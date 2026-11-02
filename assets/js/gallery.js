/**
 * THE TOWN VILLA COORG - Interactive Gallery & Lightbox
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Category Filtering
  const filterButtons = document.querySelectorAll('.filter-btn');
  const galleryItems = document.querySelectorAll('.gallery-item');

  filterButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      filterButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filterValue = btn.getAttribute('data-filter');

      galleryItems.forEach(item => {
        const itemCategory = item.getAttribute('data-category');
        if (filterValue === 'all' || itemCategory === filterValue) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      });
    });
  });

  // 2. Lightbox Modal
  const modal = document.querySelector('.lightbox-modal');
  if (!modal) return;

  const lightboxImg = modal.querySelector('.lightbox-img');
  const lightboxCaption = modal.querySelector('.lightbox-caption-text');
  const lightboxCounter = modal.querySelector('.lightbox-counter');
  const closeBtn = modal.querySelector('.lightbox-close');
  const prevBtn = modal.querySelector('.lightbox-prev');
  const nextBtn = modal.querySelector('.lightbox-next');

  let visibleImages = [];
  let currentIndex = 0;

  function updateVisibleImages() {
    visibleImages = Array.from(galleryItems).filter(item => item.style.display !== 'none');
  }

  function showImage(index) {
    if (visibleImages.length === 0) return;
    if (index < 0) index = visibleImages.length - 1;
    if (index >= visibleImages.length) index = 0;
    currentIndex = index;

    const currentItem = visibleImages[currentIndex];
    const imgEl = currentItem.querySelector('img');
    const captionEl = currentItem.querySelector('.gallery-caption');
    const src = currentItem.getAttribute('data-full') || (imgEl ? imgEl.src : '');
    const title = captionEl ? captionEl.textContent : (imgEl ? imgEl.alt : '');

    if (lightboxImg) lightboxImg.src = src;
    if (lightboxCaption) lightboxCaption.textContent = title;
    if (lightboxCounter) lightboxCounter.textContent = `${currentIndex + 1} / ${visibleImages.length}`;
  }

  function openLightbox(index) {
    updateVisibleImages();
    showImage(index);
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }

  galleryItems.forEach(item => {
    item.addEventListener('click', () => {
      updateVisibleImages();
      const index = visibleImages.indexOf(item);
      if (index !== -1) {
        openLightbox(index);
      }
    });
  });

  if (closeBtn) closeBtn.addEventListener('click', closeLightbox);
  if (prevBtn) prevBtn.addEventListener('click', () => showImage(currentIndex - 1));
  if (nextBtn) nextBtn.addEventListener('click', () => showImage(currentIndex + 1));

  // Close when clicking modal backdrop
  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      closeLightbox();
    }
  });

  // Keyboard navigation
  document.addEventListener('keydown', (e) => {
    if (!modal.classList.contains('active')) return;
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowLeft') showImage(currentIndex - 1);
    if (e.key === 'ArrowRight') showImage(currentIndex + 1);
  });

  // Touch Swipe for Mobile
  let touchStartX = 0;
  let touchEndX = 0;

  modal.addEventListener('touchstart', (e) => {
    touchStartX = e.changedTouches[0].screenX;
  }, { passive: true });

  modal.addEventListener('touchend', (e) => {
    touchEndX = e.changedTouches[0].screenX;
    handleSwipe();
  }, { passive: true });

  function handleSwipe() {
    const swipeThreshold = 50;
    if (touchEndX < touchStartX - swipeThreshold) {
      // Swiped left -> Next
      showImage(currentIndex + 1);
    }
    if (touchEndX > touchStartX + swipeThreshold) {
      // Swiped right -> Prev
      showImage(currentIndex - 1);
    }
  }
});

