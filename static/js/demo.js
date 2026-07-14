/* ============================================================
   NADI-VERSE™ | demo.js
   Form submission with loading animation
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {

  const form = document.getElementById('demo-form');
  const loadingOverlay = document.getElementById('loading-overlay');
  const loadingSteps = document.querySelectorAll('.loading-step');

  if (!form) return;

  // Loading step messages shown sequentially
  const STEP_DELAYS = [800, 1600, 2400, 3200, 4000];

  form.addEventListener('submit', (e) => {
    // Basic client-side validation
    const name = document.getElementById('id_name').value.trim();
    const age = parseInt(document.getElementById('id_age').value, 10);
    const gender = document.getElementById('id_gender').value;

    if (!name || !age || !gender) return; // Let browser/Django validation handle it

    // Show loading overlay
    if (loadingOverlay) {
      loadingOverlay.classList.add('active');
      document.body.style.overflow = 'hidden';

      // Reveal loading steps one by one
      loadingSteps.forEach((step, i) => {
        setTimeout(() => {
          step.classList.add('visible');
        }, STEP_DELAYS[i] || i * 800);
      });
    }

    // Allow normal form submit to continue
    // (overlay stays visible until page navigates away)
  });

  // If user hits back, remove overlay
  window.addEventListener('pageshow', () => {
    if (loadingOverlay) {
      loadingOverlay.classList.remove('active');
      document.body.style.overflow = '';
    }
  });

});
