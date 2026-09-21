/* No tracking, cookies or browser storage. Explicit language links win. */
(() => {
  const params = new URLSearchParams(window.location.search);
  const requested = params.get('lang');
  const isDutchBrowser = (navigator.language || 'en').toLowerCase().startsWith('nl');
  if (document.body.dataset.autoLanguage === 'true' && (requested === 'nl' || (!requested && isDutchBrowser))) {
    const target = new URL('nl/', window.location.href);
    target.hash = window.location.hash;
    window.location.replace(target.href);
    return;
  }
  document.querySelectorAll('[data-year]').forEach(el => { el.textContent = new Date().getFullYear(); });
  document.querySelectorAll('.languages a').forEach(link => {
    const target = new URL(link.href);
    target.hash = window.location.hash;
    link.href = target.href;
  });
})();
