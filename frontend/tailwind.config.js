/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './index.html',
    './js/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        'primary': '#4A90E2',
        'secondary': '#F5F7FA',
        'text': '#333333',
        'border': '#E0E6ED',
        'success': '#50E3C2',
        'error': '#D0021B',
      }
    },
    fontFamily: {
      sans: ['Pretendard', 'Noto Sans KR', 'sans-serif'],
    }
  },
  plugins: [],
}
