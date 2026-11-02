/**
 * THE TOWN VILLA COORG - WhatsApp Booking Enquiry Engine
 * Phone / WhatsApp: +91 8277268934
 */

document.addEventListener('DOMContentLoaded', () => {
  const forms = document.querySelectorAll('.booking-enquiry-form');

  forms.forEach(form => {
    const checkinInput = form.querySelector('[name="checkin"]');
    const checkoutInput = form.querySelector('[name="checkout"]');
    const nightsDisplay = form.querySelector('.nights-count-badge');
    const nameInput = form.querySelector('[name="guest_name"]');
    const guestsInput = form.querySelector('[name="guests"]');
    const villasInput = form.querySelector('[name="villas"]');
    const extraBedsInput = form.querySelector('[name="extra_beds"]');
    const messageInput = form.querySelector('[name="special_requests"]');

    // Setup dates
    const today = new Date();
    const todayStr = today.toISOString().split('T')[0];

    // Default: tomorrow for check-in, day after for checkout
    const tomorrow = new Date(today);
    tomorrow.setDate(tomorrow.getDate() + 1);
    const tomorrowStr = tomorrow.toISOString().split('T')[0];

    const dayAfter = new Date(tomorrow);
    dayAfter.setDate(dayAfter.getDate() + 1);
    const dayAfterStr = dayAfter.toISOString().split('T')[0];

    if (checkinInput) {
      checkinInput.min = todayStr;
      if (!checkinInput.value) checkinInput.value = tomorrowStr;
    }

    if (checkoutInput) {
      checkoutInput.min = tomorrowStr;
      if (!checkoutInput.value) checkoutInput.value = dayAfterStr;
    }

    function calculateNights() {
      if (!checkinInput || !checkoutInput) return 1;
      const ci = new Date(checkinInput.value);
      const co = new Date(checkoutInput.value);
      const diffTime = co - ci;
      const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
      const validDays = diffDays > 0 ? diffDays : 1;

      if (nightsDisplay) {
        nightsDisplay.textContent = `${validDays} Night${validDays > 1 ? 's' : ''}`;
      }
      return validDays;
    }

    if (checkinInput && checkoutInput) {
      checkinInput.addEventListener('change', () => {
        const nextDay = new Date(checkinInput.value);
        nextDay.setDate(nextDay.getDate() + 1);
        const nextDayStr = nextDay.toISOString().split('T')[0];
        checkoutInput.min = nextDayStr;
        if (checkoutInput.value <= checkinInput.value) {
          checkoutInput.value = nextDayStr;
        }
        calculateNights();
      });

      checkoutInput.addEventListener('change', calculateNights);
      calculateNights();
    }

    // Submit handler
    form.addEventListener('submit', (e) => {
      e.preventDefault();

      const name = nameInput ? nameInput.value.trim() : 'Guest';
      const checkin = checkinInput ? checkinInput.value : '';
      const checkout = checkoutInput ? checkoutInput.value : '';
      const nights = calculateNights();
      const guests = guestsInput ? guestsInput.value : '2';
      const villas = villasInput ? villasInput.value : '1';
      const extraBeds = extraBedsInput ? extraBedsInput.value : '0';
      const notes = messageInput ? messageInput.value.trim() : '';

      if (!checkin || !checkout) {
        alert('Please choose valid check-in and check-out dates.');
        return;
      }

      // Format Date in nice readable Indian format (DD/MM/YYYY)
      const formatDate = (dateStr) => {
        const parts = dateStr.split('-');
        if (parts.length === 3) return `${parts[2]}/${parts[1]}/${parts[0]}`;
        return dateStr;
      };

      let text = `Hello Coorg Villa,\n`;
      text += `I would like to enquire about villa booking availability in Madikeri:\n\n`;
      text += `• Guest Name: ${name || 'Prospective Guest'}\n`;
      text += `• Check-in: ${formatDate(checkin)}\n`;
      text += `• Check-out: ${formatDate(checkout)} (${nights} Night${nights > 1 ? 's' : ''})\n`;
      text += `• Villas Required: ${villas} Villa${villas > 1 ? 's' : ''}\n`;
      text += `• Guests: ${guests} Guest${guests > 1 ? 's' : ''}\n`;
      if (extraBeds && extraBeds !== '0') {
        text += `• Extra Beds: ${extraBeds}\n`;
      }
      if (notes) {
        text += `• Note / Request: ${notes}\n`;
      }
      text += `\nPlease let me know the availability, tariff, and booking details. Thank you!`;

      const encodedText = encodeURIComponent(text);
      const waUrl = `https://wa.me/918277268934?text=${encodedText}`;

      // Track event
      if (window.gtag) {
        window.gtag('event', 'submit_booking_enquiry', {
          event_category: 'Booking',
          event_label: `${villas} Villa(s), ${guests} Guests`
        });
      }

      window.open(waUrl, '_blank', 'noopener,noreferrer');
    });
  });
});

