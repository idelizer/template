/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.{html,js}",
    ".static/**/*.{html, js}",
  ],
  jit: true,
  theme: {
    extend: {},
  },
  plugins: [],
}

