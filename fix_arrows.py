with open('site/css/style.css', 'a', encoding='utf-8') as f:
    f.write('''
/* Garder les flèches du calendrier visibles même quand elles sont désactivées */
.flatpickr-calendar .flatpickr-prev-month.flatpickr-disabled,
.flatpickr-calendar .flatpickr-next-month.flatpickr-disabled {
    display: block !important;
    opacity: 0.15 !important;
    cursor: not-allowed !important;
    pointer-events: none;
}
''')
print("CSS updated")
