/* DocuFlow UI enhancements. Plain JavaScript, no dependencies. */
(function () {
  "use strict";

  /* Point every [data-df-repo] link at the repository configured in mkdocs.yml (repo_url). */
  function linkRepository() {
    var source = document.querySelector(".md-source");
    document.querySelectorAll("[data-df-repo]").forEach(function (link) {
      if (source && source.href) {
        link.href = source.href;
        link.target = "_blank";
        link.rel = "noopener";
      }
    });
  }

  /* Interactive pipeline: buttons with role="tab" switch role="tabpanel" sections. */
  function initPipeline(root) {
    var tabs = Array.prototype.slice.call(root.querySelectorAll('[role="tab"]'));
    var panels = Array.prototype.slice.call(root.querySelectorAll('[role="tabpanel"]'));
    if (!tabs.length || tabs.length !== panels.length) { return; }

    root.classList.add("df-enhanced");

    function select(index, focus) {
      tabs.forEach(function (tab, i) {
        var active = i === index;
        tab.setAttribute("aria-selected", active ? "true" : "false");
        tab.tabIndex = active ? 0 : -1;
        panels[i].hidden = !active;
      });
      if (focus) { tabs[index].focus(); }
    }

    tabs.forEach(function (tab, i) {
      tab.addEventListener("click", function () { select(i, false); });
      tab.addEventListener("keydown", function (event) {
        var next = null;
        if (event.key === "ArrowRight") { next = (i + 1) % tabs.length; }
        if (event.key === "ArrowLeft") { next = (i - 1 + tabs.length) % tabs.length; }
        if (event.key === "Home") { next = 0; }
        if (event.key === "End") { next = tabs.length - 1; }
        if (next !== null) { event.preventDefault(); select(next, true); }
      });
    });

    select(0, false);
  }

  /* Mark the landing page so CSS can remove the default content padding. */
  function markHome() {
    document.body.classList.toggle("df-home", !!document.querySelector(".df-hero"));
  }

  function init() {
    markHome();
    linkRepository();
    document.querySelectorAll("[data-df-pipeline]").forEach(initPipeline);
  }

  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(init);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
