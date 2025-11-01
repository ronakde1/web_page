document.addEventListener("DOMContentLoaded", () => {
  const button = document.querySelector(".read-more");
  if (button) {
    button.addEventListener("click", () => {
      alert("This would take you to the full article page!");
    });
  }
});