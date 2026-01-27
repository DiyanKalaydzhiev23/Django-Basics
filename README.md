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





