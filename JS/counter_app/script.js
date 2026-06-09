let count = 0;

function updateCount() {
  const countEl = document.getElementById("count");

  countEl.innerHTML =
    `<i class="fa-solid fa-hashtag"></i> ${count}`;

  countEl.classList.remove("animate");
  void countEl.offsetWidth;
  countEl.classList.add("animate");
}

function increaseCount() {
  count++;
  updateCount();
}

function decreaseCount() {
  if (count > 0) {
    count--;
    updateCount();
  }
}

function resetCount() {
  count = 0;
  updateCount();
}

function saveCount() {
  localStorage.setItem("count", count);
}

function loadCount() {
  const saved = localStorage.getItem("count");

  if (saved !== null) {
    count = Number(saved);
  }

  updateCount();
}

function applyTheme(theme) {
  const btn = document.getElementById("themeBtn");

  if (theme === "dark") {
    document.body.classList.add("dark-mode");
    btn.innerHTML =
      `<i class="fa-solid fa-sun"></i> Light`;
  } else {
    document.body.classList.remove("dark-mode");
    btn.innerHTML =
      `<i class="fa-solid fa-moon"></i> Dark`;
  }
}

function toggleTheme() {
  const isDark =
    document.body.classList.toggle("dark-mode");

  const theme = isDark ? "dark" : "light";

  localStorage.setItem("theme", theme);
  applyTheme(theme);
}

window.onload = () => {
  const savedTheme =
    localStorage.getItem("theme") || "light";

  loadCount();
  applyTheme(savedTheme);
};