# Django Basics


### Other Repos

- [Petstagram](https://github.com/DiyanKalaydzhiev23/petstagram-2026)

---

### Theory Tests

- [HTTP and Internet](https://forms.gle/SF9gSGPJta1CUkkz6)

- [Django Introduction](https://forms.gle/j4t4yWyBXu42a1uu6)

- [Urls and Views](https://forms.gle/sBKHwZEBTLqYSqABA)

- [Templates](https://forms.gle/YFignn8j3QRipiV69)

- [Forms Basics](https://forms.gle/5yoEyfecjhFnwKqEA)

- [Forms Advanced](https://forms.gle/NaT5UwYh1k1exaZb6)

- [Class Based Views Basics](https://forms.gle/ex9BNEnXxsYFB2YV7)

- [Class Based Views Advanced](https://forms.gle/RBW6bbFSHdQmeUi38)

---

# Plans

### 01. Internet and HTTP

1. Какво е интернет
   - Една голяма мрежа от устройства
   - Пример:
     - Ако ние разкачим нашия рутер и го свържем с телефона и лаптопа ни, това е някаква (мини) мрежа от 2 устройства.
     - Ако аз пусна приложение на някакъв порт на лаптопа ми, ще мога да го достъпя на телефона.
     - Ако след това свържем рутера с интернет, то това ще бъде свързване на нашата (мини) мрежа с всички останали мини мрежа, в една голяма мрежа.
   - Заражда се като научноизследователска дейност през 1969.
   - Начините, по които се свързваме са чрез:
      - Оптични кабели
      - Медни кабели
      - Телефонни клетки
      - Сателити
   - Команди за всички индивидуални мрежови интерфейси на нашата машина 
       - Mac/Linux: 
       ```bash
         ifconfig
       ```
    
       - Windows:
       ```bash
         ipconfig /all
       ```
    
       - Физически интерфейси: en0, en1, en2, en3, en4, en5, en6
       - Виртуални интерфейси: lo0, bridge0, utun0, utun1, utun2, utun3, awdl0

2. Request/Response - Client/Server
   - Ние искаме някакъв ресурс и ако имаме достъп го взимаме
   - Клиента е всяко приложение, което може да достъпи сървър
   - Сървъра е машината, която може да предоставя ресурси
   ```terminal
     curl https://softuni.bg/
   ```

3. Network Protocol
   - Стандарт, чрез който могат да комуникират 2 устройства
   - Правилата, които трябва да бъдат изпълнени, така че съвъра да може да разбере какво иска клиента, и когато върне резултат клиента да може да го разбере.
   - Често използвани протоколи:
     - HTTP:
       - Използван за зареждане на уеб страници, всяка заявка и отговор са независими.
     - TCP:
       - Гарантира, че данните се предават надеждно и в правилния ред, осигурява връзка преди предаване.
     - FTP:
       - Протокол за прехвърляне на файлове, работи в клиент-сървър модел и поддържа различни режими на трансфер.
       - Често се използва за теглене на резервно копие на база данни, главно поради големия обем на данните.
     - SSH:
       - Осигурява сигурен отдалечен достъп до мрежови устройства, криптирайки комуникацията.
     - SMTP:
       - Използваме, за да изпращаме имейли към имейл провайдъри.
     - IP:
       - Протокол за адресиране и маршрутизация на данни в мрежи, който осигурява изпращането и получаването на пакети между устройства.

4. Пакети
   - Когато сървъра и клиента си обменят данни, те ги обменят на пакети
   - Ако имаме твърде голям обем от данни те ще бъдат разделени на малки части (пакети).
   - Клиента ще раздроби данните на пакети, когато ги подава на сървъра. Той от своя страна ще ги сглоби и обратното.
   - Протокола е начина, по който, съръра и клиента разбират как да обработват пакетите.

5. IP адрес
   - Уникален идентификатор в локалната мрежа
   - В една мрежа всички IP-та трябва да са уникални
   - Поради тази причина свързвайки се с с друга мрежа, можем да имаме друго IP в нея.
   - Ако ние сме свързали няколко устойства в една мрежа, те могат да излизат под едно IP за външия свят, но вътре в самата мрежа те имат различни IP адреси
   - [What is my IP?](https://whatismyipaddress.com/#google_vignette)

6. IPv4 vs IPv6
   - v4 позволява създаането на 4.3 милиарда уникални адреса
     - 32-битови адреси
     - Пример:
       - **192.168.14.20**
       - **192.168** е мрежова част
       - **14** е подмрежа (нашата мрежа)
       - **20** е нашето устройство в мрежата
   - v6 позволява създаването на 3.4×10^38 уникални адреса
     - 128-битови адреси

7. DNS - Domain Name System
   - Грижи се да можем да достъпваме сайтове през домейн(име), а не през IP
   - IP-то се сменя, затова не можем да караме потребителте да го помнят
  
8. HTTP
   - Винаги получаваме резултат
   - Протокола на интернет
   - HTTP1/HTTP2 използват TCP/IP под себе си. HTTP3 използва QUIC протокол.
   - HTTP verb:
     - CREATE
     - POST
     - PUT
     - DELETE
     - ...
   - [Status codes](https://http.cat/)

9. URL (Uniform Resource Locator)
   - Подобно на адресите в реалния свят имаме: държава, град, квартал...
   - **http://localhost:8080/demo/html?id=26&lang=en#lecture**
   - http - протокол
   - localhost - host, domain
   - 8080 - порт
   - /demo/html - път
   - ?id=26&lang=en - query string
   - #lecture - fragment
   - https://softuni.bg:443 - можем да си спестим порта, защото https се заржда на 443 по подразбиране.
   - Можем да имаме url-и на кирилица
  
10. MIME (Multi-purpose Internet Mail Extensions)
   - Обяснява типа на данните, които се изпращат и получават

---

### 02. Django Introduction

1. Framework - Работна рамка
   - Следваме определени правила и структури.
   - Получаваме готови функции
  
2.  MVT Pattern
   - **M**odel **V**iew **T**emplate

3. Структура на Django проект
   - manage.py - entry point-a за работа с Django, с него изпълняваме command-line операции
   - projectFolder
     - settings.py - съдържа настроките на приложението
     - urls.py - място където дефинираме url-и, които да са достъпни от потребителя
     - asgi.py - setup за асинхронни заявки
     - wsgi.py - setup за синхронни заявки
   - djangoApp - всеки app се грижи за отделна част от нашия проект


4. Creation of a django app
   1. Move app to project directory (Optional)
   2. Create `urls.py` file
   3. Register the djagoApp in `settings.py`
   4. Register the urls in the project
   
   ```bash
      python manage.py runserver
   ```

5. Databases
   - За Postgres инсталираме psycopg2
   - Конфигурираме в `setting.py`
   - Създаваме база
   - Създаваме модели в `models.py`
   - `makemigrations`
   - `migrate`
  
6. Views
   - Съдържат главната бизнес логика
   - Function Based View (FBV)
   - Трябват ни:
     - Функция, която има един или повече параметри и връща отрговор
     ```python
        def index(request):
           return HttpResponse("Hello world") 
     ```
     ```python
        HttpResponse("Hello world", headers={
           "Content-Type": "application/json",
        })
     ```

7. urls
   - Създаваме си променлива с име `urlpatterns` в app/urls.py
   - В нея задаваме на какъв път, какво view да се изпълни
   ```python
      from .views import index
   
      urlpatterns = (
         path('home/', index),
      ) 
   ```
   - Добавяме си app/urls в project/urls.py
   ```python
       urlpatterns = (  
          path('admin/', admin.site.urls),
          path('', include('project_name.app_name.urls')),  
       )
   ```

8. Admin Panel
   - Django пакет
   - Започнат като third-party пакет и в последствие добавен като официален пакет
   - /admin/ - за да достъпим админ панела
   - `createsuperuser`
   - admin.py - регистрираме моделите, които искаме да могат да се манипулират в админа
  
9, Django Template Language (DTL)
   - Като динамичен HTML
   - Имаме цикли, ифове
   - Можем да рендерираме наши стойности
   - `{{ }}` - интерполация
   - `{% %}` - template tags


---

### 03. Urls and Views

1. Какво са url-ите в Django?
   - Всеки url преставлява път, на който зареждаме дадено view
   - Django ги проверява последователно за съвпадение
     
   ```python
      urlpatterns = [
         path('index/', index_view),
         path('index/', index_view_2)  # никога няма да видим index_view_2
      ]
   ```

   - В основните urls на проекта ни, трябва да включим тези от всяко наше приложение
   - Можем да сложим общ prefix, които да седи пред всеки url на даден app
     
   ```python
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('departments/', include('departments.urls')),
   ]

   ```

   - include може да приема списък от paths

2. Динамични url-и
   - Понякога искаме в url-a да динамична стойност (променяща се, примерно id)
   ```python
      path('index/<int:pk> ', index_view),
   ```
   - Типове динамични url-и
     - str
     - int
     - slug - string, които не може да има интервали и non-Ascii символи
     - path - "/some/path" - не бихме имали съвпадение в str, защото Django вижда това като отделни пътища
     - uuid
    - re_path
      - Винаги пишем в raw стринг(стринг, които няма escapes)
      - В django 2 всеки път е бил с регулярни изрази
      ```python
         re_path(r'^article/(?P<year>[0-9]{4})/', view)
         # matches year and saves it in a variable year
      ```

3. Views
   - Function Based Views
     - Приемат http заявка и връщат http отговор(или негов наследник)
     - Освен заявката могат да получават други параметри заложени в url-a
    
4. Response types
  - HttpResponse
    - Обект, който се грижи за това да се сериализира нашият отговор (да се разбие на пакети и тн.)
    - Можем да му подаваме content (съдържание)
    - Можем да му подадем status_code
      ```python
         return HttpResponse(content="Hi my name is", status=201)
      ```
  - JsonResponse
    ```python
    content = json.dumps({
      "name": "Dido",
      "age": 20
    })

    return HttpResponse(content=content, content_type="application/json")
    # or
    return JsonResponse(content,)
    ```

5. Django Shortcuts
   - **render**
     - Рендерира контекст в html template
     ```python
        return render(request, 'core/index.html', context)  # context is optional 
     ```
   - **redirect**
     - Пренасочва ни към друг url
     - Може да бъде permanent
       - Когато искаме винаги от тази страница да се пренасочва към друга
   ```python
      redirect('https://softuni.bg')  # използваме абсолютен url. защото редиректваме към друго приложение
      redirect('my_view_name', pk=10)  # използваме име на view-то, за по-добра абстракция 
   ```
   - **resolve_url**
     - Използва url resolver-a на django, за да намери url отговарящ на view или model (ако в модела има get_absolute_url)
   - get_object_or_404()
   - get_list_or_404()
   ```python
   article =  get_object_or_404(Article, pk=article_id)
   ```
   - **reverse**
     - Получава име на url, търси в регистрираните имена и връща url-а с това име
   - **reverse_lazy**
     - Използва се за конвигурация
     - Зарежда url-а, когато той съществува
     ```python 
        # settings.py
        LOGIN_URL = reverse('index') # throws an error
        LOGIN_URL = reverse_lazy('index') # throws an error
     ```

6. Django Errors
   - raise Http404
   - return HttpResponseNotFound
   - Постигат един и същ резултат
   - Можем да персонализираме 404 страницата като направум темплейт с име `404.html` 

---



### 04. Templates

1. Django Template Language(DTL)
   - Използваме, за рендерираме информацията от view-тата
   - Позволява ни да пишем html, които в зависимост от данните да бъде различен
   - Единствените езици, които Django поддържа out of the box DTL и Jinja2
   - Има други алтернативи като `Jinja2`
   - Mожем да рендредираме в html, txt, xml и тн.
   - С него правим Sever Side Rendering(SSR)
   - Настройките по подразбиране за DTL можем да намерим в `settings.py`
   ```python
      TEMPLATES = [
          {
              'BACKEND': 'django.template.backends.django.DjangoTemplates',
              'DIRS': [BASE_DIR / 'templates']
              ,
              'APP_DIRS': True,
              'OPTIONS': {
                  'context_processors': [
                      'django.template.context_processors.debug',
                      'django.template.context_processors.request',
                      'django.contrib.auth.context_processors.auth',
                      'django.contrib.messages.context_processors.messages',
                  ],
              },
          },
      ]
   ```

2. Променливи
   - Попълваме от контекста в `{{ }}`
   - Имената на променливите трябва да бъдат snake_case само букви и цифри
   - Достъпване на методи, пропъртита и индекси става чрез .
   - {{ my_list.1 }}, {{ person.full_name }}, {{ my_object.items }}
  ```python
    context = {
      "person": {
          "name": "Dido"
          "age": 20,
      },
      "person2": Person(name="Metodi", age="21 "
     }
  ```

3. Филтри
  - Използваме, за да преобразуваме нашите данни в темплейта
  - Използваме със символа `|` 
  - Някои филтри имат параметри като тях подаваме с `:` 
  - Някои built-in филтри
    - trucatechars:number - маха последните number chars и ги заменя с ...
    - truncatewords:number
    - join:seprarator - същото като ''.join(separator) в Python
    - date:format - форматира датата по желан от нас начин
    - default:value - какво да се покаже при falsy стойност
    - add:value - добавя към съществуваща стойност
    - capfirst - прави първата буква главна
 - Линк към всички филтри в Django -> [Django Template Filters](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/) 

4. Тагове
   - Цикли, проверки и други built-in действия.
   - Таговете, които рендерират html имат затварящи тагове, защото html не зачита whitespace  
   - url tag - позволява ни да не използваме hardcoded urls
   - csrf_token - генерира произволен стринг на бек енда, рендерира го във фронт-енд-а и го сравнява като направим заявка, също запазва cookie

  ```html
   <!-- Example of if, elif, else -->
    {% if user.is_authenticated %}
        <p>Welcome, {{ user.username }}!</p>
    {% elif user.is_staff %}
        <p>Welcome, staff member!</p>
    {% else %}
        <p>Welcome, guest! Please log in.</p>
    {% endif %}

    <!-- Handling empty URLs -->
    {% if url %}
        <a href="{{ url }}">Visit this link</a>
    {% else %}
        <p>No URL provided.</p>
    {% endif %}

    <!-- Example of cycle -->
    <ul>
        {% for item in items %}
            <li class="{% cycle 'row1' 'row2' %}">{{ item }}</li>
        {% endfor %}
    </ul>

    <!-- Example of lorem -->
    <p>{% lorem 3 p %}</p>
  ```

5. Static Files
   - Ресурси, които се зареждат за всеки потребител
   - Снимки, видеа, икони
   - SetUp
     ```python
        STATIC_URL = "static/"  # BASE URL - място от където достъпваме статичните ресурси
        STATICFILESDIRS = (
             BASE_DIR / 'staticfiles',  # create a folder staticfiles, usually on the level of manage. py
        )  # The place on the filesystem where staticfiles are
     ```
   - `https://localhost:8000/static/file.css` - достъпваме файл
   - `{% static 'PATH/TO/FILE' %} - static тага, заменя STATIC_URL, по този начин, ако той бъде сменен, няма да се налага да го променяме навсякъде
   - В началото на темплейта добавяме `{% load static %}`, което зарежда статичните файлове
   - При деплоймънт, django не предоставя статичните файлове, защото пускаме приложението си с gunicorn, които също не се грижи за статичните файлове
   - Тогава ни трябва още една настройка
     ```python
        STATIC_ROOT = BASE_DIR / 'staticfiles_compiled'
     ```
   - Изпълняваме командата `collectstatic`, която взима статичните файлове от всички наши и чужди приложения и ги слага на STATIC_ROOT пътя. 


6. Template Inheritance
   - Позолява ни да разширим html файл
   - Можем да го използваме за персонализирани стилове на всяка страница {% block styles %}{% endblock %} - in header
   - `base.html`
   ```html
   <html>
      <h1>Hello</h1>
      {% block content %}
      {% endblock %}
   </html>   
   ```

   - `my-extending-file.html`
   ```html
      {% extends 'base.html' %}
   
      {% block content %}
         <p>Extending code</p>
      {% endblock %}
   ```

7. Template Including
   - С цел преизползване на един html на много места, можем да го вместим/инжектираме в друг html файл
   - `{% include 'reusable-file.html %}`
   - Можем да подаваме параметри на вмъкнатия темплейт, които да достъпваме както достъпваме данните от контекста
   - `{% include 'reusable-file.html with name="Hello" %}`
  
8. Custom Filters
   - Създаваме модул в app-а ни, задължително с името `templatetags`
   - В него създаваме в Python файл, нашия филтър
   ```py
      from django import template
   
      register = template.Library()
      
      @register.filter(name='custom_title')
      def custom_title(value):
          """Capitalizes the first letter of each word, except for specified words"""
          exceptions = ['and', 'or', 'the', 'in', 'on', 'at', 'to', 'with', 'a', 'an']
          words = value.split()
          result = []
          for word in words:
              if word.lower() in exceptions and len(result) != 0:
                  result.append(word.lower())
              else:
                  result.append(word.capitalize())
          return ' '.join(result)
   ```
   - в html файла трябва да заредим файла с филтъра ни
   - `{% load my_file_name %}`
  
9. Custom Tags
   - Simple Tag - връща една стойност
  ```py
   from django import template
   
   register = template.Library()
   
   @register.simple_tag
   def simple_tag_example():
       return "This is a simple tag"
  ```
   - Includsion Tag - връща html стринг базаиран на темплейт
   ```py
      from django import template
      
      register = template.Library()
      
      @register.inclusion_tag('user_info.html', takes_context=True)
      def user_info(context, user, extra_info):
          return {
              'user': user,
              'extra_info': extra_info,
              'request': context['request']
          }

      <div class="user-info">
          <h2>User Information</h2>
          <p>Username: {{ user.username }}</p>
          <p>Email: {{ user.email }}</p>
          <p>Extra Info: {{ extra_info }}</p>
      </div>
 
      {% load my_tags %}
      
      <div>
          {% user_info user "Additional details about the user" %}
      </div>


   ```
   - Tag - връща Template Node с render функцията
   ```py

      # Register an instance of Library to register custom template tags
      register = template.Library()
      
      # Define a custom Node class for the 'uppercase' tag
      class UppercaseNode(Node):
          def __init__(self, nodelist):
              # nodelist is the content between the custom opening and closing tags
              self.nodelist = nodelist
      
          def render(self, context):
              # Render the content between the tags using the current context
              output = self.nodelist.render(context)
              # Convert the rendered content to uppercase before returning it
              return output.upper()
      
      # Register a custom template tag named "uppercase"
      @register.tag(name="uppercase")
      def do_uppercase(parser, token):
          # Parse everything between {% uppercase %} and {% enduppercase %}
          nodelist = parser.parse(('enduppercase',))
          # Remove the 'enduppercase' token from the parsing queue
          parser.delete_first_token()
          # Return an instance of the custom UppercaseNode with the parsed nodelist
          return UppercaseNode(nodelist)
   ```

10. Bootstrap
   - [Link](https://getbootstrap.com/)

---


---

### Forms Basics

1. Какво са формите
   - Начин клиента да изпраща данни на съвъра
   - Пример: search bar-а на Софтуни
   - Основни параметри на формите
     - action
       - подаваме url към, който искаме да се изпратят нашите данни
       - default value -> current_url
     - method
       - подаваме метода, който искаме да има нашата заявка
       - default value ->  GET 
       - При GET, информацията от формата се подава като query в url-a
       - При POST/PUT, информацията се подава като body
      
2. Form fields
   - Формите събират информация от input полетата в себе си
   - Полетата трябва да имат параметър name, за да можем да ги прочетем от бек енда
   - Можем да видим пратените данни в payload на request в браузъра 
  
3. Input types
   - email
   - range
   - number
   - text
   - password
   - url
   - hidden
   - radio
   - checkbox 

4. Textarea
   - Input e single-line
   - ТеxtArea е multi-line
  
5. Dropdowns
   ```html
      <select>
         <option value="1">Gaming</option>
         <option value="2 ">Reading</option>
      </select>
   ```

6. Форми в Django
   - Създаваме ги във `forms.py`
   ```py
      class EmployeeForm(forms.Form):
         first_name = forms.CharField(
               max_length=35,
               required=True,
         )
   ```

   - В темплейта
   ```html
   <form action="{% url 'index' %}" method="post" >
      {{ employee_form }}
      {% csrf_token %}
      <button>Send</button>
   </form>
   ```

   - Във view-то
   ```py
      def index(request):
         if request.method == "GET":
            context = {
               "employee_form": EmployeeForm,
            }
   
            return render(request, "web/index.html", context)
         else:
            print(request.POST)  # get the data but without any validation
            form = EmployeeForm(request.POST)

            if form.is_valid(): # starts validation process returns boolean
               print(form.cleaned_data["first_name"])
               return redirect('index')
            else:
               context = {
                  "employee_form": form,  # подаваме формата с грешките в нея
               }

               return render(reques t, "web/index.html", context)
   ```

---



### Forms Advanced

1. Django Validators
   - Трябва да е callable
   - Трябва да вдига `ValidationError` при грешка
   - Можем да ги използваме на няколко места. Пример: във форми и модели
   - Валидаторите стоят в миграциите, ако изтрием валидатора след makemigrations, миграциите няма да минават
   - Извикват се автоматично на `full_clean()` 
   - `full_clean()` се извиква при извикване на `is_valid()` на форма
   - Хубаво е валидаторите да стоят в модела, защото по този начин имаме една и съща валидация на клиента и на администрацията
   ```py
   # validator with func
   from django.core.exceptions import ValidationError

   def validate_even(value):
       if value % 2 != 0:
           raise ValidationError(
               '%(value)s is not an even number',
               params={'value': value},
           )
   ```

   ```py
   # validator with class
   from django.core.exceptions import ValidationError
   
   class EvenValidator:
       def __init__(self, message=None, code=None):
           self.message = message or '%(value)s is not an even number'
           self.code = code or 'not_even'
       
       def __call__(self, value):
           if value % 2 != 0:
               raise ValidationError(
                   self.message,
                   code=self.code,
                   params={'value': value},
               )
       
       def __repr__(self):
           return f'EvenValidator(message={self.message}, code={self.code})'
   
       def deconstruct(self):
           return (
               f"{self.__class__.__module__}.{self.__class__.__name__}",
               [],
               {'message': self.message, 'code': self.code}
           )
   ```


2. Modelform factory
      - Можем да създаваме modelForms със modelform_factory
      - Позволява ни динамично да създаваме форми
      - Можем да създаваме различни форми за различните потребители или в зависимост от  някакви променливи
      ```py
         PersonForm = modelform_factory(Person, fields=('__all__', ))
      ```


3. Персонализиране на форми
   - Можем да итерираме през всички полета в `__init__` и да ги направим readonly (това може да бъде направено с миксин)
   ```py
   # mixins.py

   class ReadOnlyFieldsMixin:
       def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)
           for field in self.fields.values():
               field.widget.attrs['readonly'] = True

   ```
   ```py
   # forms.py

   from django import forms
   from .models import Person
   
   class PersonForm(forms.ModelForm):
       class Meta:
           model = Person
           fields = ['name', 'age', 'email']
           
           labels = {  # custom labels
               'name': 'Your Name',
               'age': 'Your Age',
               'email': 'Your Email',
           }
           
           error_messages = {  # custom error messages
               'name': {
                   'required': 'This field is required.',
                   'max_length': 'Name cannot be longer than 100 characters.',
                   'unique': 'Should be unique',
               },
               'age': {
                   'required': 'This field is required.',
                   'invalid': 'Enter a valid age.',
               },
               'email': {
                   'required': 'This field is required.',
                   'invalid': 'Enter a valid email address.',
               },
           }

   ```

   - Можем да правим валидации на формата с методи с име `clean_<fieldname>`
   ```py
   # forms.py
   
   from django import forms
   from .models import Person
   from django.core.exceptions import ValidationError
   
   class PersonForm(forms.ModelForm):
       class Meta:
           model = Person
           fields = ['first_name', 'last_name', 'age', 'email']
           
   
       def clean_first_name(self):
           first_name = self.cleaned_data.get('first_name')
           if not first_name.isalpha():
               raise ValidationError('First name should contain only alphabetic characters.')
           return first_name

   ```
   - Използваме `clean` метода за логически валидации свързващи няколко полета
   ```py
       def clean(self):
        cleaned_data = super().clean()
        last_name = cleaned_data.get("last_name")
        age = cleaned_data.get("age")

        if last_name and last_name.startswith("A"):
            if age is None or age < 18:
                raise ValidationError("If your last name starts with 'A', you must be at least 18 years old.")
        
        return cleaned_data
   ```

4. Save method
   - Метод на ModelForm
   - Получава един параметър `commit` (по подразбиране True)
   ```py
       def save(self, commit=True):
        # Get the unsaved Person instance
        person = super().save(commit=False)
        
        # Custom logic before saving
        person.first_name = person.first_name.capitalize()
        person.last_name = person.last_name.capitalize()

        # Save the instance if commit is True
        if commit:
            person.save()

        # Custom logic after saving, e.g., sending a notification
        # send_notification(person)  # hypothetical function

        return person
   ```

5. Formsets
   - Позволява ни да създаваме и обработваме много форми едновременно
   - Например, ако правим quiz app, всеки въпрос може да е отделна форма
   ```py
   AuthorFormSet = modelformset_factory(Author, form=AuthorForm, extra=3)
   
   # views.py
   from django.shortcuts import render, get_object_or_404, redirect
   from .models import Book, Author
   from .forms import AuthorFormSet
   
   def manage_authors(request, book_id):
       book = get_object_or_404(Book, id=book_id)
       if request.method == 'POST':
           formset = AuthorFormSet(request.POST, queryset=book.authors.all())
           if formset.is_valid():
               authors = formset.save(commit=False)
               for author in authors:
                   author.book = book
                   author.save()
               return redirect('book_detail', book_id=book.id)
       else:
           formset = AuthorFormSet(queryset=book.authors.all())
       return render(request, 'manage_authors.html', {'formset': formset, 'book': book})
   ```

6. Стилизиране на форми
   - Визуализация
   ```py
      {{ form.as_p }}
      {{ form.as_ul }}
      {{ form.as_div }}
      {{ form.as_table }}
   ```
   - Добавяне на css класове
   ```py
      self.fields['email'].widget.attrs['class'] = 'my-css-class'
   ```
   - Обхождане на форма
   ```py
      {% for field in form %}
                  <div class="form-group">
                      <label for="{{ field.id_for_label }}">
                          {{ field.label }}
                          {% if field.field.required %}*{% endif %}
                          {# Display field properties for demonstration #}
                          (Type: {{ field.field.widget.input_type }},
                           Max Length: {{ field.field.max_length }},
                           Required: {{ field.field.required }})
                      </label>
                      <input 
                          type="{{ field.field.widget.input_type }}"
                          name="{{ field.html_name }}"
                          id="{{ field.id_for_label }}"
                          class="{{ field.field.widget.attrs.class }}"
                          placeholder="{{ field.field.widget.attrs.placeholder }}"
                          maxlength="{{ field.field.max_length }}"
                          {% if field.value %} value="{{ field.value }}"{% endif %}
                      >
                      {# Display errors if any #}
                      {% if field.errors %}
                          <div class="error">
                              {{ f ield.errors }}
                          </div>
                      {% endif %}
                  </div>
              {% endfor %}
   ```
   - Crispy Forms
     - Дават ни повече контрол върху формите
     - `pip install django-crispy-forms`
     - `pip install crispy-bootstrap4`
     - Добавяме в INSTALLED_APPS под името 'crispy_forms', 'crispy_bootstrap4'
     - В `settings.py` CRISPY_TEMPLATE_PACK = 'bootstrap4' 


7. Работа с медиа файлове
   - Видеа, снимки, аудио файлове
   - За да можем да работим с тези файлове ни трябва Pillow
   ```py
   # models.py

   class MyModel:

      image_field = models.ImageField(
         upload_to="/"
      )

   # settings.py
   MEDIA_ROOT = (
      BASE_DIR / 'mediafiles',
   )

   # views.py
   ...
   form = form(request.POST, request.FILES)

   # tempate form param
   enctype="multipart/form-data"
   ```
   
--- 


### Classed Based Views - Basics

- Защо да ползваме CBV?
  - По-чисто е
  - Позволява ни да правим наследяване
  - Получаваме абстракция
 
1. views.View
   - Базово клас вю
   ```py
   class IndexView(views.View):
      def get(self, request):
         # perform get logic

      def post(self, request):
         # perform post logic
   ```

2. Custom Class Based View
   ```py
   class BaseView:
       @classonlymethod  # позвлолява извикване само през клас
       def as_view(cls):
           def view(request, *args, **kwargs):
               self = cls()  # Create an instance of the view
               if request.method == "GET":
                   return self.get(request, *args, **kwargs)
               elif request.method == "POST":
                   return self.post(request, *args, **kwargs)
               else:
                   return HttpResponseNotAllowed(['GET', 'POST'])  # Handle unsupported methods
   
           return view
   
       def get(self, request, *args, **kwargs):
           raise NotImplementedError("GET method not implemented")
   
       def post(self, request, *args, **kwargs):
           raise NotImplementedError("POST method not implemented")
   
   class MyView(BaseView):
       def get(self, request, *args, **kwargs):
           # perform some get logic
           return HttpResponse("This is a GET response")
   
       def post(self, request, *args, **kwargs):
           # perform some post logic
           return HttpResponse("This is a POST response")

   ```

   ```py
   urlpatterns = [
      path('cbv/', MyView.as_view())  # as_view връща обект - нашето view
   ]
   ```

   - as_view
     - Връща вюто като callable
     - Може да бъде извикано с kwargs
     ```py
     urlpatterns = [
          # Redirect to 'https://www.example.com/'
          path('redirect-example/', CustomRedirectView.as_view(url='https://www.example.com/'), name='custom-redirect'),
      ]
     ```

   - dispatch
     - Използва се за викане на правилните методи спрямо рекуеста
     - Можем да го използваме за валидация, дали даден потребител има достъп до даден ресурс
     ```py
      import random
      from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotAllowed
      
      # Simulating a Django-like environment
      class SimulatedRequest:
          """A simple simulated request object."""
          def __init__(self, method):
              self.method = method.upper()
              self.user = 'SimulatedUser'  # Placeholder for user information

      class BaseView:
          def dispatch(self, request, *args, **kwargs):
              """
              Simulate the dispatch method, routing the request to the appropriate handler.
              For POST requests, check if the user has permission using a random choice.
              """
              if request.method == 'GET':
                  return self.get(request, *args, **kwargs)
              elif request.method == 'POST':
                  # Simulate permission checking
                  has_permission = random.choice([True, False])
                  print(f"Permission check for POST: {'Allowed' if has_permission else 'Denied'}")
                  
                  if has_permission:
                      return self.post(request, *args, **kwargs)
                  else:
                      return HttpResponseForbidden("You do not have permission to perform this action.")
              else:
                  return HttpResponseNotAllowed(['GET', 'POST'])
      
          def get(self, request, *args, **kwargs):
              return HttpResponse("Base GET response")
      
          def post(self, request, *args, **kwargs):
              return HttpResponse("Base POST response")

      class MyView(BaseView):
          def get(self, request, *args, **kwargs):
              return HttpResponse("MyView GET response")
      
          def post(self, request, *args, **kwargs):
              return HttpResponse("MyView POST response")
      
      # Simulating requests
      def simulate_request(view, method):
          request = SimulatedRequest(method)
          response = view.dispatch(request)
          print(f"Response to {method} request: {response.content.decode()} (Status Code: {response.status_code})\n")
      
      # Create an instance of MyView
      my_view = MyView()
      
      # Simulate GET request
      simulate_request(my_view, 'GET')
      
      # Simulate POST requests multiple times to observe permission variations
      for _ in range(3):
          simulate_request(my_view, 'POST')

     ```

3. Типове вюта
   - TemplateView - Показва темплейт 
   ```py
      class MyTemplateView(TemplateView):
      # static template
       template_name = "my_template.html"

      # dynamic template
      def get_template_names(self):
      pass

      # static context
      extra_context = {      
         "title": "hello",
      }
      
      # Dynamic context
       def get_context_data(self, **kwargs):
           # Call the base implementation first to get the default context
           context = super().get_context_data(**kwargs)
           
           # Add extra context
           context['title'] = 'My Template View'
           context['user_status'] = 'Active'
           context['random_number'] = 42
           context['items'] = ['Apple', 'Banana', 'Cherry']
           
           return context
   ```
   - RedirectView
   ```py
      from django.views.generic.base import RedirectView
      
      class MyRedirectView(RedirectView):
          url = 'https://www.example.com/'  # The URL to redirect to
   ```

   - CreateView, UpdateView, DeleteView
     - Получава модел, темплейт, success_url и полета, и генерира форма, която хендълва get и post
     - get_success_url ни позволява да взимаме динамично success_url
      ```py
         # views.py
         
         class BookCreateView(CreateView):
             model = Book
             fields = ['title', 'author', 'published_date']
             template_name = 'book_form.html'  # The template that will be used to render the form
             success_url = reverse_lazy('book-list')  # Redirect to the book list view after a successful creation
   
      ```

---



### Class Based Views - Advanced

1. ListView
   - Дава ни списък от елементи
   - В контекста се попълват като object_list и model_name_list
   ```py
   # views.py
      class FilteredBookListView(ListView):
          model = Book
          template_name = 'filtered_book_list.html'

          # за филтрации (optional)
          def get_queryset(self):
              # Filter books published after January 1, 2020
              return Book.objects.filter(published_date__gt=date(2020, 1, 1))

   ```
   - Дава ни pagination
   ```py
      class PaginatedBookListView(ListView):
          model = Book
          template_name = 'paginated_book_list.html'
          context_object_name = 'books'
          paginate_by = 10  # Number of books per page
   ```
   - Достъпване в темплейта
   - Слага page в url-a
   ```py
       <div class="pagination">
           <span class="step-links">
               {% if page_obj.has_previous %}
                   <a href="?page=1">&laquo; first</a>
                   <a href="?page={{ page_obj.previous_page_number }}">previous</a>
               {% endif %}
   
               <span class="current">
                   Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
               </span>
   
               {% if page_obj.has_next %}
                   <a href="?page={{ page_obj.next_page_number }}">next</a>
                   <a href="?page={{ page_obj.paginator.num_pages }}">last &raquo;</a>
               {% endif %}
           </span>
       </div>
   ```
   
2. Detail View
   - Подобно на list view, но работи с един обект
   <img src="https://codefellows.github.io/sea-python-401d6/_images/DetailView.png" />

3. Полезни CBV методи
   - get()
     - Описание: Този метод се използва за обработка на HTTP GET заявки. В него можете да определите логиката, която се изпълнява при получаване на GET заявка към даден URL.
   - post()
     - Описание: Този метод се използва за обработка на HTTP POST заявки. Подобно на get(), но за POST заявки, тук се дефинира логиката, която трябва да се изпълни, когато POST заявка е получена.
   
   - get_queryset()
     - Описание: Използва се за извличане на набора от данни (queryset), който ще се обработва и показва от view-то. Често се използва в CBV като ListView и DetailView, за да се определи какви данни да бъдат изведени.
     - Статична настройка: Може да бъде зададен предварително чрез статичен атрибут queryset, но чрез този метод можете динамично да персонализирате набора от данни.
       
   - get_context_data()
     - Описание: Този метод се използва за добавяне на допълнителен контекст към шаблона (template). В него можете да добавите всякакви допълнителни данни, които искате да предадете към шаблона.
     - Статична настройка: Ако няма нужда от динамичен контекст, статични контекстови данни могат да се зададат директно в extra_context атрибут на класа.
       
   - dispatch()
     - Описание: Методът dispatch() решава кой HTTP метод (например, GET или POST) да бъде използван за дадена заявка и съответно извиква съответния метод (get(), post(), и т.н.). Той е отговорен за маршрутизирането на заявката към правилния метод. Може да се изполва за роверка на достъпа на потребител
   
   - get_template_names()
     - Описание: Този метод връща списък с имена на шаблони, които трябва да се използват за рендиране на view-то. Може да се използва за динамично определяне на шаблона въз основа на определени условия.
     - Статична настройка: Статично, името на шаблона обикновено се задава чрез атрибута template_name. get_template_names() може да бъде използван за по-динамична настройка.
   - get_context_object_name()
     - Описание: Този метод се използва в изгледи като DetailView и ListView, за да се определи името на контекстовата променлива, която ще бъде използвана в шаблона. Тази променлива съдържа обекта или списъка от обекти, който се предава на шаблона.
     - Статичен заместител: Вместо да използвате get_context_object_name(), можете да зададете статично името на контекстовата променлива чрез атрибута context_object_name.
   - get_success_url()
     - Описание: Този метод се използва в изгледи като CreateView, UpdateView, и DeleteView, за да определи URL адреса, към който потребителят ще бъде пренасочен след успешното изпълнение на дадено действие (напр. създаване, обновяване или изтриване на обект).
     - Статичен заместител: Вместо да използвате get_success_url(), можете статично да зададете URL адреса чрез атрибута success_url.
   - render_to_response()
     - Описание: Този метод се използва за рендиране на шаблон с определен контекст и връщане на HttpResponse обект. Това е основният метод за рендиране в CBV.
     - Статична настройка: Ако желаете да се използва един и същ контекст и шаблон във всяко рендиране, можете да го зададете статично чрез други методи като get_context_data() и get_template_names().

4. Декоратори
   - В джанго често се използват за промяна на поведението на даден метод.
   - login_required
   - permission_required
---



