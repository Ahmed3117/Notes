   

## شرح Sitemap، وكيفية إضافتها لموقعك بالشكل الصحيح - ووردبريس بالعربية

------

حتى يتم فهرسة صفحات موقعك في جوجل بالشكل الصحيح، تحتاج إلى إنشاء  خريطة للموقع (Sitemap) لموقعك وتقديم هذه الصفحة إلى جوجل لفهرسات صفحات  موقعك، سواءًا كانت مقالات (كما هو في مواقع الأخبار والمدونات)، أو كانت  منتجات (كما هو في المتاجر الإلكترونية).

في هذه المقالة سنتعرف على شرح Sitemap  وكيف تقوم بإضافتها إلى موقعك  حتى يتم فهرسة موقعك بالشكل الصحيح، ويكون مهيئًا للظهور في نتائج البحث.

![img](https://www.wpar.net/wp-content/uploads/2021/06/%D8%AA%D8%B9%D8%B1%D9%81_%D8%B9%D9%84%D9%89_%D8%B4%D8%B1%D8%AD_%D9%88%D8%A5%D8%B6%D8%A7%D9%81%D8%A9_%D8%AE%D8%A7%D8%B1%D8%B7%D8%A9_%D9%85%D9%88%D9%82%D8%B9%D9%83_%D8%A8%D8%A7%D9%84%D8%B4%D9%83%D9%84_%D8%A7%D9%84%D8%B5%D8%AD%D9%8A%D8%AD_01-1024x576.png)

**محتويات المقالة:**

------

### ما هو ملف sitemap ؟

خريطة الموقع (sitemap) هي عبارة عن ملف XML يحتوي على كل روابط صفحات  وصور وفيديوهات الموقع واي ملفات اخرى ، ويقوم بتنظيمها بشكل يسهل فهمه لأي محرك بحث مثل جوجل، حيث يقرأ محرك البحث الملف ويقوم بالوصول لكل صفحات  موقعك بناء على المعلومات التي بهذا الملف .

 ملفات XML بصفة عامة صممت لنقل وتخزين البيانات وهي ملفات تشبه ملفات  HTML التي تظهر صفحاتك على المتصفح، ولكن الفرق بين XML و HTML انها ملفات  ناقلة للمعلومات بصورة منظمة وليست مسؤولة عن ظهورها بشكل رسومي ( مثل شكل  صفحة هذا المقال).
وبالتالي فإن ملفات XML تظهر نفس ذات المحتويات الخاصة بالموقع ولكن بشكل منظم لمحركات البحث.

 أقصى عدد من الروابط يمكن ان يحتويها ملف الـ sitemap الواحد 50 الف  رابط ولمعرفة شكل الروابط داخل ال sitemap لموقعنا مثلا انظر الشكل التالي ، يمكن أن يكون هناك اكثر من ملف لخريطة الموقع بسبب عدم السماح الا ب 50  الف رابط في الملف الواحد فيتم التحايل وعمل اكثر من ملف

![img](https://www.wpar.net/wp-content/uploads/2021/01/sitemap1.jpg)

 إذا قمت بمعاينة ملف المصدر لملف XML بالضغط على كليك يمين، ثم ضغطت على View Page source 

![img](https://www.wpar.net/wp-content/uploads/2021/01/viewPageSource.jpg)

ستجد أن شكل ملف المصدر لخريطة الموقع كالتالي

![img](https://www.wpar.net/wp-content/uploads/2021/01/sitemap1source.jpg)

لاحظ انه بسبب ان الحد الاقصى للروابط التي يمكن أن توجد في ملف خريطة  الموقع الواحد لا يمكن أن تتعدى خمسين الف رابط فيتم تقسيم خريطة الموقع  على عدة ملفات انظر الشكل التالي كمثال على تقسيم الملفات في موقعنا

![img](https://www.wpar.net/wp-content/uploads/2021/01/2020-12-24_17-23-50.jpg)

------

### شرح ملف robots.txt

 حتى يتم فهرسة صفحات موقعك من قبل محرك البحث، فإنه يتم إرسال  عناكب ( bot أو robot أو spider )  للوصول إلى المواقع لمعرفة محتواها وفهرستها في قواعد بياناتها لتظهر لنا عند البحث في المحرك عن أي موضوع .

يساعد ملف robots.txt لعمل هذه المهمة، حيث يستخدم للإشارة إلى محركات  البحث بالصفحات التي يجب الزحف لها (crawl) والصفحات التي لا تحتاج إلى  فهرستها بمحرك البحث،  بمعنى اخر ماهي الصفحات المسموح لجوجل بعمل فهرسة  لها والممنوع عمل فهرسة لها.

يمتلك كل محرك بحث العناكب الخاصة به، فموقع جوجل له العناكب الخاصة به  ومحرك Bing له العناكب الخاصة به، ونفس الأمر  لأدوات التحليل والفهرسة  (Alexa مثلًا) يمتلك ايضا عناكب خاصة به.

في بعض الأحيان قد تحتاج إلى حجب عناكب الزحف والفهرسة لبعض المواقع  لأجل زيادة أمان موقعك من تحليله لدى المنافسين، أو لعدم الوصول لبعض  الصفحات التي لا تريد فهرستها في محرك البحث. 

 يتم كتابة اكواد خاصة داخل ملف robots.txt كالمثال التالي وهو كود يمنع أي عملية زحف للموقع وفهرسة ما به

\#Code to not allow any search engines!

\#Code to not allow any search engines! User-agent: * Disallow: /

```
#Code to not allow any search engines!
User-agent: *
Disallow: /
```

لإيقاف الزحف عن مجلد معين يكتب الكود التالي

\# Blocks robots from specific folder / directory

\# Blocks robots from specific folder / directory User-agent: * Disallow: /wp-includes/

```
# Blocks robots from specific folder / directory
User-agent: *
Disallow: /wp-includes/
```

------

### كيفية إنشاء  sitemap  لموقعك 

إذا كان موقعك يعتمد على الووردبريس، فتستطيع إنشاء Sitemap بسهولة من  خلال بعض الإضافات مثل  Google XML Sitemaps أو اضافة SEO by yoast .
سنشرح هذه المهمة من خلال إضافة  [yoast](https://www.wpar.net/yoast-seo/)  التي تستخدمها غالبًا لتحسين [سيو موقعك](https://www.wpar.net/wordpress-seo/)، فيمكنك بنفس الإضافة  عمل خريطة للموقع بأسلوب سهل. فبعد [تنصيب وتفعيل الإضافة على موقعك](https://www.wpar.net/how-to-install-wordpress-plugin/)،  ستذهب إلى  القائمة الفرعية والذهاب إلى تبويبة الإضافة، ثم اختيار عام كالتالي 

![img](https://www.wpar.net/wp-content/uploads/2021/01/GoTositemap-1024x735.jpg)

سيظهر لك عدة تبويبات نختار منها التبويب مميزات كالشكل التالي

![img](https://www.wpar.net/wp-content/uploads/2021/01/clickFeatures-1024x735.jpg)

يظهر لك عدة أزرار قم باختيار تشغيل خرائط الموقع sitemap كالتالي

![img](https://www.wpar.net/wp-content/uploads/2021/01/EnableSitemap-1024x735.jpg)

لمعرفة ماهي خرائط الموقع التي تم إنشاؤها اضغط علامة السؤال بجانب خرائط الموقع

![img](https://www.wpar.net/wp-content/uploads/2021/01/ClickQuestionMark-1024x735.jpg)

يظهر لك رابط لرؤية خرائط الموقع كاملة

![img](https://www.wpar.net/wp-content/uploads/2021/01/SitemapShow-1024x735.jpg)

اضغط الرابط تظهر لك الملفات كاملة على متصفحك

![img](https://www.wpar.net/wp-content/uploads/2021/01/BrowserShowSitemap-1024x262.jpg)

وبهذا تكون قد أنشأت ملف Sitemap لموقعك بسهولة

------

### كيفية إنشاء ملف robots.txt لموقعك 

كما تحدثنا عن أهمية هذا الملف واستخداماته، فيمكنك أيضًا إنشاء الملف  بالإعتماد على إضافة Virtual Robots.txt أو إضافة SEO by yoast و سنشرح لك  الطريقة أيضًا باستخدام إضافة  yoast  فبعد تفعيل الإضافة، اذهب الى  القائمة الفرعية واختا أدوات كما بالشكل التالي

![img](https://www.wpar.net/wp-content/uploads/2021/01/SEOTools-1024x735.jpg)

يظهر لك الشاشة التالية وتحتوي على محرر الملف قم بالضغط عليه.

![img](https://www.wpar.net/wp-content/uploads/2021/01/ClickToCreateFile-1024x735.jpg)

الان قم بالضغط على زر انشاء ملف robots.txt 

![img](https://www.wpar.net/wp-content/uploads/2021/01/CreateFileRobote-1024x735.jpg)

يظهر لك المحرر ومنه يمكنك اضافة الاكواد التي تريد ثم حفظ الملف

![img](https://www.wpar.net/wp-content/uploads/2021/01/EditeAndSaveFile-1024x735.jpg)

**ملحوظة**: لا تستخدم أكثر من إضافة تقوم بتفعيل XML site map لموقعك، لأنه قد يحدث تعارض بين هذه الإضافات، أو يكون لموقعك أكثر من خريطة مما يربك محركات البحث في فهم موقعك.

------

### ربط خريطة الموقع بجوجل

لارشفة الموقع بالطريقة الصحيحة يتم اضافة الموقع من خلال ادوات مشرفي المواقع  (google search console) بطريقة سهلة.
 اذهب إلى [Google Search Console](https://search.google.com/search-console/about) ثم ستظهر لك شاشة الترحيب، ومنها يمكنك الضغط على **البدء الآن**

![img](https://www.wpar.net/wp-content/uploads/2021/01/clickStartSearchConsole-1024x735.jpg)

تظهر لك أدوات مشرفي المواقع جوجل كالتالي قم بعمل اضافة لموقعك حتى تتمكن من ربطه مع خريطة الموقع

![img](https://www.wpar.net/wp-content/uploads/2021/01/addSiteToConsole-1-1024x451.jpg)

تظهر لك شاشة ربط النطاق (اسم موقعك بالكامل) قم بادخال اسم الموقع ثم اضغط متابعة

![img](https://www.wpar.net/wp-content/uploads/2021/01/addSiteAndConfirme-edited.jpg)

من الشريط الجانبي اختار ملفات sitemap كالتالي

![img](https://www.wpar.net/wp-content/uploads/2021/01/clickSitemapAtConsol-edited.jpg)

ستظهر لك شاشة ادخال اسم الخريطة وإرسالها لجوجل حتى يتم الربط

![img](https://www.wpar.net/wp-content/uploads/2021/01/addSitemapThenSend-edited.jpg)

يستطيع الان جوجل الزحف الى موقعك ومعرفة كل الصفحات التي يجب عليه  ارشفتها (تذكر أنه عندما تقوم باضافة صفحة جديدة مثل مقال جديد أو منتج  جديد يجب عليك ادخالها يدويا من Google Search Console لسرعة أرشفته وعدم  انتظار معرفة عناكب جوجل لما هو جديد من اضافه ).

------

### الأسئلة الشائعة

**هل يمكن عمل ملف sitemap يدويا ؟**
يمكن عمل ذلك ولكن هذا سيأخذ منك وقتًا ومجهودًا أكبر حسب حجم موقعك، في حال إعتمادك على  الووردبريس يفضّل استخدام الإضافات الجاهزة  كما أعطينا بعض الأمثلة  (Google xml sitemap أو Yoast)، لكن

**أين يمكن وضع ملف robots.txt ؟**
الملف يتم وضعهداخل  المجلد الرئيسي public_html الموجود على الخادم (يتم ذلك من خلال الذهاب  الى لوحة تحكم الموقع cpanel ثم الى مدير File Manager ثم رفع الملف داخل  المجلد public_html). أما في حالة استخدام إحدى الإضافات فيتم إضافتها  تلقائيًا في المكان المذكور.

**هل الملف robots.txt يمنع وصول أي أحد للملفات والمجلدات ؟**
ا هو فقط يمنع الارشفة ولمنع الوصول لاي ملف او مجلد يستخدم ملف آخر يسمى .htaccess 

--------

## Adding robots.txt to a Django site :

Yesterday we added sitemaps as part of SEO. Today, we  need a file called robots.txt to tell bots where they can't go on our  website.  

Not all bots are going to use this file, but most of the good ones will.

We can start by creating a new file called robots.txt and add it in your template folder.

Add the following content to it:

```
User-agent: * 
Disallow: /admin/
Disallow: /api/
```

Here I say that all robots "*" should not go into /admin/ and /api/. You can add more pages here if you want to.

Then, the only thing we need to do is to add this to the url patterns:

```
# Import function from Django
from django.views.generic.base import TemplateView

# Append to url patterns
path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
```

And that's it, you can now go to http://127.0.0.1:8000/robots.txt

---

## Creating a simple sitemap :

Sitemaps are an important part of SEO. In this guide, I will show you how to generate one using Django.            

### Set up

The first thing we need to do in order to use sitemaps, is to include a Django app. Django has built in functionality for this, so we just  need to add this to the list of installed apps.

Open up settings.py and add this line to the list:

```
'django.contrib.sitemaps',
```

### The sitemaps

Inside the main folder of your project, create a file called "sitemaps.py" (Together with urls.py, settings.py, etc).

Add the following contents to it:

```
from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from blog.models import Post

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['frontpage'', 'contact']
    
    def location(self, item):
        return reverse(item)

class PostSitemap(Sitemap):
    def items(self):
        return Post.objects.all()
    
    def lastmod(self, obj):
        return obj.created_at
```

First, I just want to say that this is just an example of how this  could be done. In my case, I have two static views (frontpage and  contact) and my blog has a model called Post. I get all the post objects and add a last modified value to it.

I use the "reverse" function from Django to get the full path to the posts and pages.

### Adding the sitemaps to the urls

Already we're at the last step of this procedure.

Inside the urls.py file, we need to import a few things.

```
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap, PostSitemap
```

The first thing we import here is the functionality from Django and then we import the two sitemaps we just created.

Next, we need to make a dictionary with the two sitemaps:

```
sitemaps = {'static': StaticViewSitemap, 'post': PostSitemap}
```

Then, we can just append it as a path inside the url patterns.

```
path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
```

If you now go to http://127.0.0.1:8000/sitemap.xml, you should see the two sitemaps.

​          