import re

def compile_ru_to_py(russian_code):
    """Compiles Russian keywords to English Python"""
    
    translation_dict = {
        # Conditions
        'если': 'if',
        'иначе': 'else',
        'иначе_если': 'elif',
        
        # Loops
        'для': 'for', 
        'в': 'in',
        'пока': 'while',
        'прервать': 'break',
        'продолжить': 'continue',
        
        # Functions
        'функция': 'def',
        'вернуть': 'return',
        'лямбда': 'lambda',
        
        # Classes
        'класс': 'class',
        'сам': 'self',
        
        # Other
        'и': 'and',
        'или': 'or', 
        'не': 'not',
        'Пусто': 'None',
        'Истина': 'True',
        'Ложь': 'False'
    }
    
    # Replace keywords
    for ru, en in translation_dict.items():
        russian_code = re.sub(r'\b' + ru + r'\b', en, russian_code)
    
    return russian_code

def compile_file(input_file, output_file=None):
    """Compiles .ru.py file to .py file"""
    with open(input_file, 'r', encoding='utf-8') as f:
        ru_code = f.read()
    
    py_code = compile_ru_to_py(ru_code)
    
    if output_file is None:
        output_file = input_file.replace('.ru.py', '.py')
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(py_code)
    
    print(f"Compiled: {input_file} → {output_file}")
    return output_file
