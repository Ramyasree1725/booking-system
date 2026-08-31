(function () {
  'use strict';

  const csrfToken = getCookie('csrftoken');
  let calendar;
  let resources = [];

  function getCookie(name) {
    let v = null;
    if (document.cookie) {
      document.cookie.split(';').forEach(c => {
        c = c.trim();
        if (c.startsWith(name + '=')) v = decodeURIComponent(c.substring(name.length + 1));
      });
    }
    return v;
  }

  async function api(url, options = {}) {
    const opts = {
      credentials: 'same-origin',
      headers: {
        'Content-Type': 'application/json',
        ...(csrfToken ? { 'X-CSRFToken': csrfToken } : {}),
        ...(options.headers || {}),
      },
      ...options,
    };
    const res = await fetch(url, opts);
    const data = await res.json().catch(() => ({}));
    if (!res.ok) {
      const msg = data.detail || data.non_field_errors?.[0] || JSON.stringify(data) || res.statusText;
      throw new Error(typeof msg === 'string' ? msg : JSON.stringify(msg));
    }
    return data;
  }

  async function loadResources() {
    try {
      const data = await api('/api/resources/resources/');
      resources = data.results || data;
      const filter = document.getElementById('resourceFilter');
      const modal = document.getElementById('modalResource');
      resources.forEach(r => {
        const opt1 = new Option(r.name, r.id);
        const opt2 = new Option(r.name, r.id);
        filter.appendChild(opt1);
        if (modal) modal.appendChild(opt2);
      });
    } catch (e) {
      console.warn('Could not load resources (login may be required):', e.message);
    }
  }

  function initCalendar() {
    const el = document.getElementById('calendar');
    if (!el) return;

    calendar = new FullCalendar.Calendar(el, {
      initialView: 'timeGridWeek',
      headerToolbar: {
        left: 'prev,next today',
        center: 'title',
        right: 'dayGridMonth,timeGridWeek,timeGridDay,listWeek',
      },
      height: 'auto',
      slotMinTime: '07:00:00',
      slotMaxTime: '22:00:00',
      allDaySlot: false,
      nowIndicator: true,
      selectable: true,
      selectMirror: true,
      events: async (info, success, failure) => {
        try {
          let url = `/api/bookings/calendar/?start=${info.startStr}&end=${info.endStr}`;
          const resId = document.getElementById('resourceFilter')?.value;
          if (resId) url += `&resource=${resId}`;
          const events = await api(url);
          success(events);
        } catch (e) {
          console.error(e);
          success([]);
        }
      },
      select: (info) => {
        const modal = document.getElementById('bookingModal');
        if (!modal) return;
        const form = document.getElementById('bookingForm');
        form.start_datetime.value = toLocalInput(info.start);
        form.end_datetime.value = toLocalInput(info.end);
        new bootstrap.Modal(modal).show();
      },
      eventClick: (info) => {
        const p = info.event.extendedProps;
        alert(
          `${info.event.title}\n` +
          `Status: ${info.event.extendedProps.status || info.event.status || ''}\n` +
          (p.description ? `Notes: ${p.description}\n` : '') +
          (p.user ? `Booked by: ${p.user}` : '')
        );
      },
    });
    calendar.render();

    document.getElementById('resourceFilter')?.addEventListener('change', () => {
      calendar.refetchEvents();
    });
  }

  function toLocalInput(d) {
    const pad = n => String(n).padStart(2, '0');
    return `${d.getFullYear()}-${pad(d.getMonth()+1)}-${pad(d.getDate())}T${pad(d.getHours())}:${pad(d.getMinutes())}`;
  }

  function fromLocalInput(s) {
    // Send as ISO with timezone offset
    const d = new Date(s);
    return d.toISOString();
  }

  document.getElementById('submitBooking')?.addEventListener('click', async () => {
    const form = document.getElementById('bookingForm');
    const errBox = document.getElementById('bookingError');
    errBox.classList.add('d-none');
    const payload = {
      resource_id: parseInt(form.resource_id.value, 10),
      title: form.title.value,
      description: form.description.value,
      start_datetime: fromLocalInput(form.start_datetime.value),
      end_datetime: fromLocalInput(form.end_datetime.value),
      attendees: parseInt(form.attendees.value, 10) || 1,
    };
    try {
      await api('/api/bookings/', { method: 'POST', body: JSON.stringify(payload) });
      bootstrap.Modal.getInstance(document.getElementById('bookingModal')).hide();
      form.reset();
      calendar.refetchEvents();
    } catch (e) {
      errBox.textContent = e.message;
      errBox.classList.remove('d-none');
    }
  });

  document.addEventListener('DOMContentLoaded', () => {
    loadResources().then(initCalendar);
  });
})();
