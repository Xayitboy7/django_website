$('.roman__wrapper').slick({
    slidesToShow: 5,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
});

$('.block__wrapper').slick({
    slidesToShow: 2,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2500,
});

$('.stix__wrapper').slick({
    dots: true,
    slidesToShow: 2,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 3000,
});

$('.roman-stix').slick({
    dots: true,
    slidesToShow: 2,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
}); 

const wrapper = document.querySelector('.wrapper-popup')
const loginLink = document.querySelector('.login-link')
const registLink = document.querySelector('.regst-link')
const btnPopup = document.querySelector('.Login-popup')
const close = document.querySelector('.icon-close')

registLink.addEventListener('click', () => {
    wrapper.classList.add('active')
})

loginLink.addEventListener('click', () => {
    wrapper.classList.remove('active')
})

btnPopup.addEventListener('click', () => {
    wrapper.classList.add('active-popup')
})

close.addEventListener('click', () => {
    wrapper.classList.remove('active-popup')
})








const express = require('express');
const app = express();

// Обработчик для URL-адреса /search
app.get('/search', (req, res) => {
  // Получение параметра "query" из URL-адреса запроса
  const searchQuery = req.query.query;

  // Здесь вы можете реализовать логику обработки поискового запроса
  // Например, выполнить поиск в базе данных или в другом источнике данных

  // Вернуть результаты поиска в формате JSON
  const searchResults = [
    { title: 'Результат 1', url: 'http://example.com/result1' },
    { title: 'Результат 2', url: 'http://example.com/result2' },
    { title: 'Результат 3', url: 'http://example.com/result3' }
  ];

  res.json(searchResults);
});

// Запуск сервера
app.listen(3000, () => {
  console.log('Сервер запущен на порту 3000');
});