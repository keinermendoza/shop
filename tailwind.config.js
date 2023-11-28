/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./assets/js/*.js",
    "./**/templates/**/*.{html, js}", 
    "./**/templates/**/components/*.{html, js}"
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

