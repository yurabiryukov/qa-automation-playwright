from playwright.sync_api import expect, Page
import pytest


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):
        # Переходим на страницу с курсами
        chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        # Проверяем наличие текста Courses
        courses_text = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_text).to_have_text('Courses')

        # Проверяем наличие текста There is no results
        there_is_no_results_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        expect(there_is_no_results_text).to_have_text('There is no results')

        # Проверяем наличие иконки пустого списка курсов
        empty_view_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
        expect(empty_view_icon).to_be_visible()

        # Проверяем наличие текста
        empty_view_description_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
        expect(empty_view_description_text).to_have_text('Results from the load test pipeline will be displayed here')




