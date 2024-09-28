/** @type {import('tailwindcss').Config} */
export default {
  //配置tailwind的应用范围
  //在这里我们配置了tailwind应用到index.html文件和src目录下所有.vue和.js文件
  content: ["./index.html", "./src/**/*.{vue,js,ts}"],
  theme: {
    extend: {},
  },
  // plugins: [require('tailwindcss-animated')],
  plugins: [
    // eslint-disable-next-line no-undef
    require('tailwindcss-animated')
  ],
};