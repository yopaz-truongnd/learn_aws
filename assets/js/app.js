/**
 * AWS Certified Solutions Architect Associate (SAA-C03) — Study Hub
 * Application Script: Language Switcher, Theme Detection & Mermaid Renderer
 */

// 1. Immediately set language attribute to prevent UI flashing
(function () {
  try {
    var saved = localStorage.getItem('aws_study_lang') || 'vi';
    document.documentElement.setAttribute('data-lang', saved);
    document.documentElement.setAttribute('lang', saved);
  } catch (e) {}
})();

var mermaidRenderCounter = 0;

/**
 * Render all Mermaid diagrams on page according to active language and theme
 */
async function renderAllMermaid() {
  if (typeof mermaid === 'undefined') return;

  var isDark =
    document.documentElement.getAttribute('data-theme') === 'dark' ||
    (!document.documentElement.getAttribute('data-theme') &&
      window.matchMedia &&
      window.matchMedia('(prefers-color-scheme: dark)').matches);

  mermaid.initialize({
    startOnLoad: false,
    theme: isDark ? 'dark' : 'neutral',
    securityLevel: 'loose',
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
    themeVariables: isDark
      ? {
          darkMode: true,
          background: '#262524',
          primaryColor: '#1d3347',
          primaryTextColor: '#ecebe8',
          primaryBorderColor: '#6db3f2',
          lineColor: '#a3a09a',
          secondaryColor: '#2d2b2a',
          tertiaryColor: '#1c1b1a'
        }
      : {
          darkMode: false,
          background: '#ffffff',
          primaryColor: '#E5F2FC',
          primaryTextColor: '#2C2C2B',
          primaryBorderColor: '#2783DE',
          lineColor: '#7D7A75',
          secondaryColor: '#F9F8F7',
          tertiaryColor: '#F0EFED'
        }
  });

  var currentLang = document.documentElement.getAttribute('data-lang') || 'vi';
  var diagrams = document.querySelectorAll('.mermaid-diagram');

  for (var i = 0; i < diagrams.length; i++) {
    var diag = diagrams[i];
    var srcEl =
      diag.querySelector('.mermaid-src.lang-' + currentLang) ||
      diag.querySelector('.mermaid-src');
    if (!srcEl) continue;

    var code = srcEl.textContent.trim();
    var outEl = diag.querySelector('.mermaid-output');
    if (!outEl) continue;

    try {
      mermaidRenderCounter++;
      var renderId = 'mermaid_svg_' + i + '_' + mermaidRenderCounter;
      var res = await mermaid.render(renderId, code);
      outEl.innerHTML = res.svg;
    } catch (err) {
      console.error('Mermaid render error at index ' + i + ':', err);
    }
  }
}

/**
 * Set active language across UI and update stored preference
 * @param {'vi' | 'en'} lang 
 */
function setLanguage(lang) {
  try {
    document.documentElement.setAttribute('data-lang', lang);
    document.documentElement.setAttribute('lang', lang);
    localStorage.setItem('aws_study_lang', lang);
  } catch (e) {}

  document.querySelectorAll('.lang-btn').forEach(function (btn) {
    btn.classList.toggle('active', btn.getAttribute('data-lang-val') === lang);
  });

  renderAllMermaid();
}

// Make globally accessible for onclick handlers
window.setLanguage = setLanguage;
window.renderAllMermaid = renderAllMermaid;

// 2. Initialize buttons & diagrams once DOM is ready
document.addEventListener('DOMContentLoaded', function () {
  try {
    var lang = localStorage.getItem('aws_study_lang') || 'vi';
    setLanguage(lang);
  } catch (e) {
    renderAllMermaid();
  }
});

// 3. React to OS Dark/Light mode transitions
if (window.matchMedia) {
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function () {
    renderAllMermaid();
  });
}


/**
 * Study Mode: Toggle Focus on Exam Traps only
 */
function toggleExamFocus(btn) {
  document.body.classList.toggle('study-focus-exam');
  var active = document.body.classList.contains('study-focus-exam');
  if (btn) btn.classList.toggle('active', active);
}

/**
 * Study Mode: Toggle Flashcard Mode (blur answers until hovered)
 */
function toggleHideAnswers(btn) {
  document.body.classList.toggle('study-hide-answers');
  var active = document.body.classList.contains('study-hide-answers');
  if (btn) btn.classList.toggle('active', active);
}

window.toggleExamFocus = toggleExamFocus;
window.toggleHideAnswers = toggleHideAnswers;
