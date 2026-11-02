/**
 * THE TOWN VILLA COORG - Components & Year Updater
 */

document.addEventListener('DOMContentLoaded', () => {
  // Update year in footer dynamically
  const yearEl = document.getElementById('current-year');
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }
});

