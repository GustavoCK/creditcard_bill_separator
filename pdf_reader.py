from PyPDF2 import PdfReader


def filter_pdf_text(page_text):
    words_list = (page_text.replace(',', '.').splitlines())
    print(words_list)
    final_list = []
    temp_list = []
    index = 0

    while index < (len(words_list) - 1):
        temp_list.clear()
        while index < (len(words_list) - 1):
            if words_list[index] == ' ':
                words_list.pop(index)
                break

            temp_list.append(words_list[index])
            index += 1
        final_list.append(temp_list.copy())

    final_list.pop(0)
    final_list.pop(len(final_list)-1)

    return final_list


list_of_lists = []

list_of_lists.extend(filter_pdf_text((PdfReader("Creditcard-Bill.pdf").pages[0]).extract_text()))

