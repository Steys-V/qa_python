from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    # def test_add_new_book_add_two_books(self):
    #     # создаем экземпляр (объект) класса BooksCollector
    #     collector = BooksCollector()
    #
    #     # добавляем две книги
    #     collector.add_new_book('Гордость и предубеждение и зомби')
    #     collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    #
    #     # проверяем, что добавилось именно две
    #     # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
    #     assert len(collector.get_books_rating()) == 2

    @pytest.mark.parametrize('book_name', ['Война и мир', '1984', 'Гарри Поттер'])
    def test_add_new_book(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre
        assert collector.books_genre[book_name] == ''

    @pytest.mark.parametrize('book_name', ['Книга А','Книга Б'])
    def test_add_new_book_has_no_genre(self,book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert collector.get_book_genre(book_name) == ''


    def test_add_new_book_name_too_long(self):
        collector = BooksCollector()
        long_name = 'А' * 41
        collector.add_new_book(long_name)
        assert long_name not in collector.books_genre

    def test_add_new_book_empty_name(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert '' not in collector.books_genre

    @pytest.mark.parametrize ('genre', ['Фантастика','Ужасы','Детективы','Мультфильмы','Комедии'])
    def test_set_book_genre(self,genre):
        collector = BooksCollector()
        collector.add_new_book('Тестовая книга')
        collector.set_book_genre('Тестовая книга', genre)
        assert collector.get_book_genre('Тестовая книга') == genre

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 1', 'Ужасы')
        collector.set_book_genre('Книга 2', 'Ужасы')
        books = collector.get_books_with_specific_genre('Ужасы')
        assert 'Книга 1' in books
        assert 'Книга 2' in books
        assert len(books) == 2

    @pytest.mark.parametrize('age_genre',['Ужасы','Детективы'])
    def test_books_with_age_rating_not_for_children(self,age_genre):
        collector = BooksCollector()
        collector.add_new_book('Тестовая книга')
        collector.set_book_genre('Тестовая книга', age_genre)
        children_books = collector.get_books_for_children()
        assert 'Тестовая книга' not in children_books

    @pytest.mark.parametrize('book_name',['Книга 1','Книга 2','Книга 3'])
    def test_add_book_in_favorites(self,book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.delete_book_from_favorites('Книга')
        assert 'Книга' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_book_in_favorites('Книга 1')
        collector.add_book_in_favorites('Книга 2')
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 2
        assert 'Книга 1' in favorites
        assert 'Книга 2' in favorites