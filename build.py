from pathlib import Path
from datetime import date
import html
import json
import re
import shutil

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
ASSETS = DIST / "assets"
CATALOG_PATH = ROOT / "product-catalog-source.json"

if not CATALOG_PATH.exists():
    shutil.copy2(DIST / "products-source.json", CATALOG_PATH)
catalog_source = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
DIST.mkdir(parents=True, exist_ok=True)
ASSETS.mkdir(parents=True, exist_ok=True)

# Keep the published directory focused on this design and its images.
for child in DIST.iterdir():
    if child.name == "assets":
        continue
    if child.is_dir():
        shutil.rmtree(child)
    else:
        child.unlink()
for legacy in ["chireh-equipment-catalog.html", "app.js", "data.js", "style.css"]:
    stale = ASSETS / legacy
    if stale.exists():
        stale.unlink()

DETAILS = {
    "CRP-600": {
        "slug": "crp-600",
        "title": "آسیاب رینگی پنوماتیکی آزمایشگاهی CRP-600",
        "category": "آسیاکنی و پودرکنی",
        "image": "product_laboratory-pneumatic-ring-mill-crp-600.webp",
        "intro": "آماده‌سازی هم‌زمان چند نمونهٔ معدنی، با شش مجموعهٔ آسیاب مستقل در یک دستگاه.",
        "paragraphs": [
            "CRP-600 برای پودرکردن و کاهش ابعاد نمونه‌های خشک سنگ، کانی و مواد معدنی طراحی شده است. شش مجموعهٔ هاون مستقل، امکان آماده‌سازی هم‌زمان چند نمونه را در یک چرخه فراهم می‌کنند.",
            "هر هاون ظرفیتی برابر با ۱۰۰ میلی‌لیتر دارد. مجموعهٔ استاندارد از فولاد MO-40 سخت‌کاری‌شده ساخته می‌شود و سامانهٔ قفل پنوماتیکی، تایمر دیجیتال و درب‌های محافظ مجهز به میکروسوئیچ در ساختار دستگاه در نظر گرفته شده‌اند.",
            "دانه‌بندی کمتر از ۷۵ میکرون در شرایط مناسب قابل دستیابی است؛ نتیجهٔ واقعی به نوع ماده و شرایط کار بستگی دارد. خوراک پیشنهادی کمتر از ۲ میلی‌متر و حداکثر اندازهٔ مجاز خوراک ۵ میلی‌متر است."
        ],
        "features": [
            "شش هاون مستقل، هرکدام با ظرفیت مفید ۱۰۰ میلی‌لیتر",
            "آماده‌سازی هم‌زمان نمونه‌ها در یک چرخهٔ کاری",
            "مجموعهٔ استاندارد هاون از فولاد MO-40 سخت‌کاری‌شده",
            "قفل پنوماتیکی با فشار هوای موردنیاز ۵ تا ۶ بار",
            "تایمر دیجیتال با توقف خودکار",
            "دو درب محافظ با میکروسوئیچ مستقل"
        ],
        "specs": [
            ["مدل دستگاه", "CRP-600"],
            ["تعداد هاون", "۶ عدد"],
            ["ظرفیت مفید هر هاون", "۱۰۰ میلی‌لیتر"],
            ["ظرفیت مفید مجموع هاون‌ها", "۶۰۰ میلی‌لیتر"],
            ["مقدار معمول نمونه در هر هاون", "۱۰۰ تا ۱۵۰ گرم"],
            ["حداکثر ابعاد مجاز خوراک", "۵ میلی‌متر؛ خوراک پیشنهادی کمتر از ۲ میلی‌متر"],
            ["دانه‌بندی قابل دستیابی", "کمتر از ۷۵ میکرون در شرایط مناسب"],
            ["جنس استاندارد مجموعهٔ هاون", "فولاد MO-40 سخت‌کاری‌شده"],
            ["توان الکتروموتور", "۲٫۲ کیلووات"],
            ["برق ورودی پایه", "۳۸۰ ولت، ۵۰ هرتز، سه‌فاز"],
            ["فشار پنوماتیک موردنیاز", "۵ تا ۶ بار"],
            ["محدودهٔ تنظیم تایمر", "۱ ثانیه تا ۹۹ دقیقه"],
            ["ابعاد کلی", "۱۳۶۰ × ۹۳۰ × ۱۱۴۵ میلی‌متر"],
            ["وزن تقریبی", "حدود ۵۰۰ کیلوگرم"]
        ],
        "faqs": [
            ["CRP-600 چند نمونه را هم‌زمان آسیاب می‌کند؟", "این مدل شش هاون مستقل دارد و می‌تواند شش نمونه را در یک چرخهٔ کاری آماده کند."],
            ["اندازهٔ خوراک مناسب برای CRP-600 چقدر است؟", "خوراک پیشنهادی کمتر از ۲ میلی‌متر است و حداکثر اندازهٔ مجاز خوراک ۵ میلی‌متر اعلام شده است."],
            ["جنس هاون دستگاه قابل انتخاب است؟", "پیکربندی استاندارد از فولاد MO-40 سخت‌کاری‌شده است. گزینه‌های SPK و استنلس استیل SS-420 نیز قابل سفارش‌اند."],
            ["دانه‌بندی خروجی دستگاه چقدر است؟", "کمتر از ۷۵ میکرون در شرایط مناسب قابل دستیابی است. نتیجه به جنس نمونه و شرایط عملیاتی بستگی دارد."]
        ]
    },
    "CJC-200": {
        "slug": "cjc-200",
        "title": "سنگ‌شکن فکی آزمایشگاهی CJC-200",
        "category": "خردایش",
        "image": "product_laboratory-jaw-crusher-cjc-200.webp",
        "intro": "برای خردایش اولیهٔ نمونه‌های خشک سنگ و مواد معدنی و تنظیم پیوستهٔ دهانهٔ خروجی.",
        "paragraphs": [
            "سنگ‌شکن فکی CJC-200 برای کاهش ابعاد اولیهٔ نمونه‌های خشک و سخت طراحی شده است. صفحات فکی ثابت و متحرک، نمونه را در فضای خردایش میان خود فشرده می‌کنند.",
            "دهانهٔ خروجی دستگاه به‌صورت مکانیکی و پیوسته در بازهٔ صفر تا ۳۰ میلی‌متر تنظیم می‌شود. صفحات استاندارد از فولاد منگنزی ساخته شده‌اند و قابلیت تعویض دارند.",
            "ابعاد دهانهٔ ورودی ۹۰ × ۹۰ میلی‌متر است. ظرفیت برآوردی حدود ۳۰۰ کیلوگرم بر ساعت اعلام شده؛ مقدار واقعی به ویژگی نمونه و تنظیم دستگاه بستگی دارد."
        ],
        "features": [
            "دهانهٔ ورودی ۹۰ × ۹۰ میلی‌متر",
            "تنظیم مکانیکی و پیوستهٔ دهانهٔ خروجی از صفر تا ۳۰ میلی‌متر",
            "صفحات لاینر فکی قابل تعویض",
            "صفحات استاندارد از فولاد منگنزی",
            "مناسب برای خردایش اولیهٔ نمونه‌های خشک و سخت"
        ],
        "specs": [
            ["مدل دستگاه", "CJC-200"],
            ["ابعاد دهانهٔ ورودی", "۹۰ × ۹۰ میلی‌متر"],
            ["حداکثر ابعاد مجاز خوراک", "کمتر از ۹۰ میلی‌متر"],
            ["تنظیم دهانهٔ خروجی", "صفر تا ۳۰ میلی‌متر"],
            ["ظرفیت برآوردی", "حدود ۳۰۰ کیلوگرم بر ساعت"],
            ["جنس استاندارد صفحات فکی", "فولاد منگنزی"],
            ["توان الکتروموتور", "۱٫۵ کیلووات"],
            ["برق ورودی پایه", "۳۸۰ ولت، ۵۰ هرتز، سه‌فاز"],
            ["ابعاد کلی", "۴۵۰ × ۹۰۰ × ۱۱۶۰ میلی‌متر"],
            ["وزن تقریبی", "حدود ۳۰۰ کیلوگرم"]
        ],
        "faqs": [
            ["حداکثر اندازهٔ خوراک ورودی CJC-200 چقدر است؟", "ابعاد دهانهٔ ورودی ۹۰ × ۹۰ میلی‌متر است و حداکثر ابعاد مجاز خوراک کمتر از ۹۰ میلی‌متر اعلام شده است."],
            ["دهانهٔ خروجی دستگاه قابل تنظیم است؟", "بله؛ دهانهٔ خروجی به‌صورت مکانیکی و پیوسته در بازهٔ صفر تا ۳۰ میلی‌متر تنظیم می‌شود."],
            ["صفحات فکی از چه جنسی هستند؟", "جنس استاندارد صفحات لاینر فکی فولاد منگنزی است."]
        ]
    },
    "CBM": {
        "slug": "cbm-series",
        "title": "آسیاب گلوله‌ای آزمایشگاهی سری CBM",
        "category": "آسیاکنی و پودرکنی",
        "image": "product_laboratory-ball-mill-cbm-series.webp",
        "intro": "آسیاکنی ناپیوستهٔ خشک یا تر، در چهار مدل با ابعاد مخزن و ظرفیت متفاوت.",
        "paragraphs": [
            "آسیاب گلوله‌ای سری CBM برای نرمایش نمونه‌های سنگ، کانی و مواد معدنی در مقیاس آزمایشگاهی طراحی شده است. چرخش مخزن و حرکت گلوله‌های فولادی ضدسایش، کاهش ابعاد ذرات را در یک آزمون ناپیوسته ممکن می‌کنند.",
            "این سری در مدل‌های CBM-200، CBM-250، CBM-300 و CBM-350 عرضه می‌شود. حداکثر ابعاد خوراک در مدل‌ها ۱۰ میلی‌متر است و ظرفیت برآوردی مواد خشک، بسته به مدل، از ۱ تا ۹ کیلوگرم در هر نوبت متغیر است.",
            "دستگاه برای آسیاکنی خشک و تر قابل استفاده است. زمان کار با تایمر دیجیتال تنظیم می‌شود و دستگاه پس از پایان زمان تعیین‌شده به‌طور خودکار متوقف می‌شود."
        ],
        "features": [
            "چهار مدل با مخزن‌های ۲۰۰، ۲۵۰، ۳۰۰ و ۳۵۰ میلی‌متری",
            "قابلیت آسیاکنی خشک و تر به‌صورت ناپیوسته",
            "حداکثر ابعاد خوراک ۱۰ میلی‌متر",
            "گلوله‌های فولادی ضدسایش",
            "تایمر دیجیتال با توقف خودکار"
        ],
        "specs": [
            ["مدل‌ها", "CBM-200، CBM-250، CBM-300 و CBM-350"],
            ["ابعاد داخلی مخزن", "۲۰۰ × ۲۰۰ تا ۳۵۰ × ۳۵۰ میلی‌متر، بسته به مدل"],
            ["حداکثر ابعاد مجاز خوراک", "۱۰ میلی‌متر"],
            ["ظرفیت برآوردی مواد خشک", "۱ تا ۹ کیلوگرم در هر نوبت، بسته به مدل"],
            ["جرم کل بار گلوله‌ای", "۱۲ تا ۶۳ کیلوگرم، بسته به مدل"],
            ["جنس گلوله‌ها", "فولاد ضدسایش"],
            ["سرعت مخزن", "۵۷ تا ۷۰ دور بر دقیقه، بسته به مدل"],
            ["توان الکتروموتور", "۰٫۳۷ تا ۰٫۷۵ کیلووات، بسته به مدل"],
            ["شرایط آزمون", "خشک و تر"],
            ["کنترل سیکل", "تایمر دیجیتال با توقف خودکار"]
        ],
        "faqs": [
            ["آیا سری CBM برای آسیاکنی خشک و تر مناسب است؟", "بله؛ این سری برای آسیاکنی خشک و تر به‌صورت ناپیوسته طراحی شده است."],
            ["تفاوت مدل‌های CBM-200 تا CBM-350 چیست؟", "ابعاد مخزن، سرعت، توان و ظرفیت برآوردی مواد خشک با توجه به مدل تغییر می‌کند."],
            ["حداکثر اندازهٔ خوراک چقدر است؟", "حداکثر ابعاد مجاز خوراک برای سری CBM برابر با ۱۰ میلی‌متر اعلام شده است."]
        ]
    },
    "CSPI": {
        "slug": "cspi",
        "title": "آسیاب آزمایشگاهی CSPI",
        "category": "آسیاکنی و پودرکنی",
        "image": "product_laboratory-mill-cspi.webp",
        "intro": "یک مجموعه برای اجرای دو روش آزمون SPI کلاسیک و SGI بازنگری‌شده.",
        "paragraphs": [
            "آسیاب آزمایشگاهی CSPI برای سنجش قابلیت آسیاشوندگی کانسنگ و تهیهٔ داده‌های موردنیاز مطالعات طراحی و بهینه‌سازی مدارهای آسیاب نیمه‌خودشکن (SAG) طراحی شده است.",
            "این دستگاه امکان اجرای دو روش آزمون SPI کلاسیک و SGI بازنگری‌شده را فراهم می‌کند. برای هر روش، مجموعهٔ گلولهٔ مستقل در نظر گرفته شده و سرعت مخزن با اینورتر تنظیم می‌شود.",
            "در هر آزمون، جرم اسمی نمونهٔ خشک ۲ کیلوگرم است. تایمر دیجیتال با توقف خودکار و فایل محاسباتی اختصاصی Excel، ثبت داده‌ها و محاسبهٔ شاخص‌های آزمون را پشتیبانی می‌کنند."
        ],
        "features": [
            "اجرای آزمون SPI کلاسیک و SGI بازنگری‌شده",
            "جرم نمونهٔ خشک ۲ کیلوگرم در هر آزمون",
            "دو مجموعهٔ گلولهٔ مستقل، هرکدام ۵ کیلوگرم",
            "تنظیم سرعت مخزن تا حداکثر ۵۴ دور بر دقیقه",
            "تایمر دیجیتال با توقف خودکار",
            "فایل محاسباتی اختصاصی برای ثبت داده‌ها"
        ],
        "specs": [
            ["مدل دستگاه", "CSPI"],
            ["روش‌های آزمون", "SPI کلاسیک و SGI بازنگری‌شده"],
            ["جرم نمونهٔ ورودی", "۲ کیلوگرم"],
            ["جرم هر مجموعهٔ بار گلوله‌ای", "۵ کیلوگرم"],
            ["قطر گلوله‌های آزمون SPI", "۲۵٫۴ میلی‌متر"],
            ["قطر گلوله‌های آزمون SGI", "۳۱٫۷۵ میلی‌متر"],
            ["سرعت مخزن", "حداکثر ۵۴ دور بر دقیقه"],
            ["توان الکتروموتور", "۰٫۳۷ کیلووات"],
            ["برق ورودی پایه", "۲۲۰ ولت، ۵۰ هرتز، تک‌فاز؛ ورودی اینورتر"],
            ["گیربکس", "حلزونی سری NMRV"],
            ["ابعاد داخلی مخزن", "۳۰۴٫۸ × ۱۰۱٫۶ میلی‌متر"],
            ["کنترل سیکل", "تایمر دیجیتال با توقف خودکار"]
        ],
        "faqs": [
            ["CSPI چه آزمون‌هایی را اجرا می‌کند؟", "این دستگاه امکان اجرای آزمون SPI کلاسیک و SGI بازنگری‌شده را در یک مجموعه فراهم می‌کند."],
            ["جرم نمونه در هر آزمون چقدر است؟", "جرم اسمی نمونهٔ خشک در هر آزمون ۲ کیلوگرم است."],
            ["سرعت مخزن چگونه تنظیم می‌شود؟", "تنظیم سرعت از طریق اینورتر انجام می‌شود و حداکثر سرعت اعلام‌شده ۵۴ دور بر دقیقه است."]
        ]
    },
    "CST-L24": {
        "slug": "cst-l24",
        "title": "میز لرزان آزمایشگاهی CST-L24",
        "category": "جدایش مواد معدنی",
        "image": "product_CST-L24.webp",
        "intro": "بررسی جدایش ثقلی تر با تنظیم مستقل شیب، طول کورس و سرعت حرکت صفحه.",
        "paragraphs": [
            "میز لرزان CST-L24 برای بررسی جدایش ثقلی تر، پرعیارسازی کانسنگ‌ها و مطالعهٔ رفتار مواد معدنی در مقیاس آزمایشگاهی طراحی شده است.",
            "مکانیزم ویلفلی مدل B13، حرکت رفت‌وبرگشتی صفحه را با جریان عرضی آب ترکیب می‌کند و امکان هدایت محصولات به سه بخش کنسانتره، محصول میانی و باطله را فراهم می‌سازد.",
            "شیب عرضی و طولی صفحه مستقل تنظیم می‌شوند. طول کورس قابل تغییر است و سرعت حرکت با اینورتر کنترل می‌شود. ظرفیت‌های درج‌شده، حداکثر مقادیر اعلام‌شده برای صفحهٔ استاندارد درشت‌دانه و صفحهٔ مخصوص ریزدانه‌اند."
        ],
        "features": [
            "مکانیزم ویلفلی (Wilfley) مدل B13",
            "صفحهٔ فایبرگلاس با ریفل‌های یکپارچه",
            "تنظیم مستقل شیب عرضی و طولی",
            "تنظیم طول کورس و کنترل سرعت با اینورتر",
            "دو مسیر مستقل آب‌رسانی",
            "جمع‌آوری سه محصول: کنسانتره، محصول میانی و باطله"
        ],
        "specs": [
            ["مدل دستگاه", "CST-L24"],
            ["مکانیزم عملکرد", "ویلفلی (Wilfley)، مدل B13"],
            ["ابعاد صفحه", "۱۳۰۰ × ۶۲۰ میلی‌متر"],
            ["جنس صفحه", "فایبرگلاس"],
            ["ظرفیت برآوردی صفحهٔ استاندارد درشت‌دانه", "حداکثر ۱۱۵ کیلوگرم بر ساعت"],
            ["ظرفیت برآوردی صفحهٔ مخصوص ریزدانه", "حداکثر ۹۰ کیلوگرم بر ساعت"],
            ["سرعت نامی مکانیزم", "۳۷۵ دور بر دقیقه در فرکانس ۵۰ هرتز"],
            ["توان الکتروموتور", "۰٫۳۷ کیلووات"],
            ["برق ورودی اینورتر", "تک‌فاز، ۲۲۰ ولت، ۵۰ هرتز"],
            ["ابعاد کلی", "۲۲۰۰ × ۷۰۰ × ۱۳۰۰ میلی‌متر"],
            ["وزن تقریبی", "حدود ۱۴۰ کیلوگرم"]
        ],
        "faqs": [
            ["CST-L24 چه نوع جدایشی انجام می‌دهد؟", "این دستگاه برای بررسی جدایش ثقلی تر در مقیاس آزمایشگاهی استفاده می‌شود."],
            ["محصولات دستگاه چگونه جمع‌آوری می‌شوند؟", "لاندر چنددهانه با تیغه‌های قابل تنظیم، هدایت و جمع‌آوری کنسانتره، محصول میانی و باطله را ممکن می‌کند."],
            ["ظرفیت خوراک دستگاه چقدر است؟", "حداکثر ظرفیت برآوردی صفحهٔ استاندارد درشت‌دانه ۱۱۵ و صفحهٔ مخصوص ریزدانه ۹۰ کیلوگرم بر ساعت است. مقدار واقعی به ویژگی‌های خوراک و شرایط تنظیم بستگی دارد."]
        ]
    },
    "CCG-L40": {
        "slug": "ccg-l40",
        "title": "تغلیظ‌کنندهٔ گریز از مرکز آزمایشگاهی CCG-L40",
        "category": "جدایش مواد معدنی",
        "image": "product_CCG-L40.webp",
        "intro": "آزمون نیمه‌پیوستهٔ جدایش ثقلی و بررسی کانی‌های سنگین در مقیاس آزمایشگاهی.",
        "paragraphs": [
            "CCG-L40 برای بررسی جدایش ثقلی و ارزیابی بازیابی طلا و کانی‌های سنگین در مقیاس آزمایشگاهی به‌کار می‌رود. کاسهٔ در حال دوران، نیروی گریز از مرکز ایجاد می‌کند و ذرات بر پایهٔ رفتارشان در بستر جدایش تفکیک می‌شوند.",
            "دستگاه در روش نیمه‌پیوسته کار می‌کند. پس از پایان خوراک‌دهی و توقف روتور، کنسانتره جداگانه جمع‌آوری می‌شود. کاسهٔ جدایش از تفلون (PTFE) ساخته شده و برای تخلیهٔ کنسانتره و نظافت از مجموعه جدا می‌شود.",
            "محدودهٔ دانه‌بندی خوراک ۱۰ تا ۵۰۰ میکرومتر و شتاب گریز از مرکز قابل تنظیم از صفر تا ۲۰۰ G اعلام شده است. فشار آب نیز در بازهٔ صفر تا ۳۵ PSI تنظیم می‌شود."
        ],
        "features": [
            "جدایش ثقلی نیمه‌پیوسته در مقیاس آزمایشگاهی",
            "محدودهٔ دانه‌بندی خوراک ۱۰ تا ۵۰۰ میکرومتر",
            "شتاب گریز از مرکز قابل تنظیم از صفر تا ۲۰۰ G",
            "کاسهٔ جدایش تفلونی (PTFE) و قابل جداسازی",
            "فایل Excel برای ثبت و ارزیابی نتایج آزمون"
        ],
        "specs": [
            ["مدل دستگاه", "CCG-L40"],
            ["روش جدایش", "نیمه‌پیوسته (SB)"],
            ["حداکثر نرخ خوراک", "۳۰۰ کیلوگرم بر ساعت"],
            ["محدودهٔ دانه‌بندی خوراک", "۱۰ تا ۵۰۰ میکرومتر"],
            ["محدودهٔ شتاب گریز از مرکز", "صفر تا ۲۰۰ G"],
            ["محدودهٔ قابل تنظیم فشار آب", "صفر تا ۳۵ PSI"],
            ["توان الکتروموتور", "۰٫۳۷ کیلووات"],
            ["برق ورودی پایه", "تک‌فاز، ۲۲۰ ولت، ۵۰ هرتز"],
            ["ابعاد کلی", "۳۱۵ × ۴۹۵ × ۵۱۵ میلی‌متر"],
            ["وزن تقریبی", "حدود ۶۰ کیلوگرم"]
        ],
        "faqs": [
            ["CCG-L40 چه کاربردی دارد؟", "این دستگاه برای بررسی جدایش ثقلی و بازیابی کانی‌های سنگین، از جمله طلا، در مقیاس آزمایشگاهی استفاده می‌شود."],
            ["روش عملکرد دستگاه پیوسته است؟", "CCG-L40 برای آزمون نیمه‌پیوسته طراحی شده است. کنسانتره پس از پایان خوراک‌دهی و توقف روتور جمع‌آوری می‌شود."],
            ["محدودهٔ دانه‌بندی خوراک چقدر است؟", "محدودهٔ اعلام‌شده برای خوراک ۱۰ تا ۵۰۰ میکرومتر است."]
        ]
    }
}

IMAGE_BY_MODEL = {
    "CRP-600": "product_laboratory-pneumatic-ring-mill-crp-600.webp",
    "CJC-200": "product_laboratory-jaw-crusher-cjc-200.webp",
    "CBM": "product_laboratory-ball-mill-cbm-series.webp",
    "CSPI": "product_laboratory-mill-cspi.webp",
    "CST-L24": "product_CST-L24.webp",
    "CCG-L40": "product_CCG-L40.webp"
}

def esc(value):
    return html.escape(str(value), quote=True)

def get_model(title):
    if "Bond Mill" in title:
        return "Bond Mill"
    for model in DETAILS:
        if model in title:
            return model
    match = re.search(r"\b[A-Z]{2,6}(?:-[A-Z0-9]+)+\b", title)
    if match:
        return match.group(0)
    match = re.search(r"\b(CBM|CSPI)\b", title)
    return match.group(1) if match else ""

def category_for(title):
    if "سنگ‌شکن" in title:
        return ("خردایش", "crushing")
    if "آسیاب" in title:
        return ("آسیاکنی", "grinding")
    if "تقسیم" in title or "همزن" in title:
        return ("آماده‌سازی نمونه", "sample")
    if "شیکر سرند" in title:
        return ("دانه‌بندی", "sizing")
    return ("جدایش", "separation")

products = []
for index, item in enumerate(catalog_source):
    title = item.get("alt", "").strip()
    if not title:
        continue
    model = get_model(title)
    cat_label, cat_key = category_for(title)
    detail = DETAILS.get(model)
    img = IMAGE_BY_MODEL.get(model, "product-" + str(index) + ".webp")
    route = "/products/" + detail["slug"] + "/" if detail else "/contact/?product=" + __import__("urllib.parse").parse.quote(title)
    products.append({
        "title": title,
        "model": model,
        "category": cat_label,
        "category_key": cat_key,
        "image": img,
        "route": route,
        "detail": detail
    })

def product_card(product, compact=False):
    label = product["model"] or "تجهیز آزمایشگاهی"
    link_label = "مشاهده مشخصات" if product["detail"] else "استعلام این تجهیز"
    return (
        '<article class="product-card" data-product-card data-category="' + esc(product["category_key"]) + '">'
        '<a class="product-card-image" href="' + esc(product["route"]) + '" aria-label="' + esc(link_label + " " + product["title"]) + '">'
        '<img src="/assets/' + esc(product["image"]) + '" alt="' + esc(product["title"]) + '" loading="lazy">'
        '<span class="product-card-category">' + esc(product["category"]) + '</span></a>'
        '<div class="product-card-body"><p class="product-code">' + esc(label) + '</p>'
        '<h3><a href="' + esc(product["route"]) + '">' + esc(product["title"]) + '</a></h3>'
        '<a class="text-link" href="' + esc(product["route"]) + '">' + link_label + '</a></div></article>'
    )

def product_schema(detail):
    return {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": detail["title"],
        "description": detail["intro"],
        "brand": {"@type": "Brand", "name": "چیره فرآور گستر"}
    }

def organization_schema():
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "چیره فرآور گستر",
        "url": "https://chirehfg.com/",
        "logo": "https://chirehfg.com/assets/uploads/setting/4695b0b0ae106dfcb084658e9b99f21f.png",
        "telephone": ["02155448318", "09006140897"],
        "email": ["sales@chirehfg.com", "info@chirehfg.com"],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "شهرک صنعتی چهاردانگه، خیابان ۱۴، پلاک ۴",
            "addressLocality": "تهران",
            "addressCountry": "IR"
        }
    }

def header():
    return '''
    <div class="utility-bar"><div class="container utility-inner">
      <span>تجهیزات آزمایشگاهی فرآوری مواد معدنی</span>
      <div class="utility-links"><a href="tel:+982155448318">۰۲۱ ۵۵۴۴ ۸۳۱۸</a><span class="utility-separator"></span><a href="mailto:sales@chirehfg.com">sales@chirehfg.com</a></div>
    </div></div>
    <header class="site-header"><div class="container header-inner">
      <button class="menu-toggle" type="button" aria-label="بازکردن فهرست" aria-expanded="false" aria-controls="primary-nav"><span></span><span></span><span></span></button>
      <a class="brand" href="/" aria-label="چیره فرآور گستر، صفحهٔ اصلی">
        <span class="brand-mark"><svg viewBox="0 0 48 48" role="img" aria-label=""><path d="M24 3 43 14v20L24 45 5 34V14L24 3Z" fill="none" stroke="currentColor" stroke-width="2.3"/><path d="M24 3v21m0 0 19-10M24 24 5 14m19 10v21" fill="none" stroke="currentColor" stroke-width="2.3"/><path d="m15 18 9-5 9 5v11l-9 5-9-5V18Z" fill="currentColor" opacity=".18"/></svg></span>
        <span class="brand-copy"><strong>چیره فرآور گستر</strong><small>مهندسی فرآوری مواد معدنی</small></span>
      </a>
      <nav class="primary-nav" id="primary-nav" aria-label="ناوبری اصلی">
        <a href="/" data-nav="home">خانه</a>
        <details class="nav-products">
          <summary data-nav="products" aria-expanded="false" aria-controls="products-mega">
            <span>محصولات</span><i class="nav-chevron" aria-hidden="true"></i>
          </summary>
          <div class="mega-menu" id="products-mega" role="region" aria-label="دسته‌بندی محصولات">
            <section class="mega-intro" aria-labelledby="mega-intro-title">
              <span class="mega-kicker"><i aria-hidden="true"></i>کاتالوگ تجهیزات</span>
              <h2 id="mega-intro-title">مسیر فرآوری را از مرحلهٔ درست آغاز کنید.</h2>
              <p>برای هر نمونه و هدف آزمون، دستهٔ تجهیز مناسب را پیدا کنید.</p>
              <div class="mega-process" aria-label="مراحل فرآوری">
                <span>آماده‌سازی</span><b aria-hidden="true">←</b><span>خردایش</span><b aria-hidden="true">←</b><span>جدایش</span>
              </div>
              <a class="mega-all-link" href="/products/"><span>مشاهدهٔ همهٔ محصولات</span><b aria-hidden="true">←</b></a>
            </section>

            <section class="mega-categories" aria-labelledby="mega-category-title">
              <div class="mega-heading">
                <div><span class="mega-overline">دسته‌بندی تجهیزات</span><h3 id="mega-category-title">در کدام مرحله هستید؟</h3></div>
                <span class="mega-count">۵ گروه تجهیز</span>
              </div>
              <div class="mega-links">
                <a class="mega-category" href="/products/?category=sample">
                  <span class="mega-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none"><path d="m12 3 8 4.5v9L12 21l-8-4.5v-9L12 3Z"/><path d="m4.5 7.8 7.5 4.3 7.5-4.3M12 12.2V21"/></svg></span>
                  <span class="mega-copy"><strong>آماده‌سازی نمونه</strong><small>تقسیم، همگن‌سازی و آماده‌سازی</small></span><b class="mega-arrow" aria-hidden="true">←</b>
                </a>
                <a class="mega-category" href="/products/?category=crushing">
                  <span class="mega-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none"><path d="m4 17 4.8-7 3.3 4.1 2.7-3.5L20 17H4Z"/><path d="M5 20h14M7 5l3 2-2 2"/></svg></span>
                  <span class="mega-copy"><strong>خردایش</strong><small>کاهش ابعاد اولیهٔ ماده</small></span><b class="mega-arrow" aria-hidden="true">←</b>
                </a>
                <a class="mega-category" href="/products/?category=grinding">
                  <span class="mega-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="8.5"/><path d="M8 14.5 14.5 8 17 10.5 10.5 17 8 14.5Z"/><path d="m7 7 2 2m7 7 1 1"/></svg></span>
                  <span class="mega-copy"><strong>آسیاکنی و پودرکنی</strong><small>نرمایش و آماده‌سازی برای آزمون</small></span><b class="mega-arrow" aria-hidden="true">←</b>
                </a>
                <a class="mega-category" href="/products/?category=sizing">
                  <span class="mega-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none"><path d="M4 6h16M6 10h12M8 14h8M10 18h4"/><path d="M6 4v4m12-4v4"/></svg></span>
                  <span class="mega-copy"><strong>دانه‌بندی</strong><small>سرند و کنترل توزیع اندازه</small></span><b class="mega-arrow" aria-hidden="true">←</b>
                </a>
                <a class="mega-category" href="/products/?category=separation">
                  <span class="mega-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none"><path d="M4 7c2.1-2 4.1-2 6.2 0s4.1 2 6.2 0S20.5 5 22 6"/><path d="M4 12c2.1-2 4.1-2 6.2 0s4.1 2 6.2 0 4.1-2 5.6-1"/><path d="M4 17c2.1-2 4.1-2 6.2 0s4.1 2 6.2 0 4.1-2 5.6-1"/></svg></span>
                  <span class="mega-copy"><strong>جدایش مواد معدنی</strong><small>بررسی و بازیابی کانی‌های ارزشمند</small></span><b class="mega-arrow" aria-hidden="true">←</b>
                </a>
              </div>
            </section>

            <a class="mega-feature" href="/products/crp-600/" aria-label="مشاهدهٔ مشخصات آسیاب رینگی پنوماتیکی آزمایشگاهی CRP-600">
              <span class="mega-feature-tag">محصول منتخب</span>
              <span class="mega-feature-art"><img src="/assets/product_laboratory-pneumatic-ring-mill-crp-600.webp" alt="" loading="lazy"><span class="mega-feature-badge">۶ هاون مستقل</span></span>
              <span class="mega-feature-copy"><small>آسیاب رینگی پنوماتیکی</small><strong>CRP-600</strong><em>مشاهدهٔ مشخصات <b aria-hidden="true">←</b></em></span>
            </a>
          </div>
        </details>
        <a href="/services/" data-nav="services">خدمات</a>
        <a href="/articles/" data-nav="articles">دانشنامه</a>
        <a href="/about/" data-nav="about">دربارهٔ ما</a>
        <a href="/contact/" data-nav="contact">تماس</a>
      </nav>
      <a class="header-cta" href="/contact/"><span>مشاورهٔ فنی</span><b aria-hidden="true">+</b></a>
    </div></header>
    '''

def footer():
    return '''
    <section class="footer-cta" aria-labelledby="footer-cta-title">
      <div class="container footer-cta-inner">
        <div class="footer-cta-copy">
          <span class="footer-cta-kicker"><i aria-hidden="true"></i> مشاورهٔ فنی</span>
          <h2 id="footer-cta-title">برای انتخاب تجهیز، از نمونه و هدف آزمون شروع کنیم.</h2>
          <p>نوع نمونه، اندازهٔ خوراک و نتیجهٔ موردنیازتان را با ما در میان بگذارید.</p>
        </div>
        <div class="footer-cta-actions">
          <a class="footer-cta-button" href="/contact/"><span>درخواست مشاوره</span><b aria-hidden="true">←</b></a>
          <a class="footer-cta-phone" href="tel:+982155448318"><small>تماس مستقیم با دفتر</small><strong>۰۲۱ ۵۵۴۴ ۸۳۱۸</strong></a>
        </div>
      </div>
    </section>
    <footer class="site-footer">
      <div class="container footer-grid">
        <div class="footer-brand">
          <a class="brand brand-light" href="/" aria-label="چیره فرآور گستر، صفحهٔ اصلی">
            <span class="brand-mark"><svg viewBox="0 0 48 48" aria-hidden="true"><path d="M24 3 43 14v20L24 45 5 34V14L24 3Z" fill="none" stroke="currentColor" stroke-width="2.3"/><path d="M24 3v21m0 0 19-10M24 24 5 14m19 10v21" fill="none" stroke="currentColor" stroke-width="2.3"/></svg></span>
            <span class="brand-copy"><strong>چیره فرآور گستر</strong><small>مهندسی فرآوری مواد معدنی</small></span>
          </a>
          <p>طراحی و ساخت تجهیزات آزمایشگاهی برای آماده‌سازی نمونه، خردایش، آسیاکنی و جدایش مواد معدنی.</p>
          <div class="footer-brand-note"><i aria-hidden="true"></i><span>از نمونهٔ خام تا دادهٔ قابل اتکا</span></div>
        </div>

        <nav class="footer-column" aria-label="دسترسی سریع">
          <h2>دسترسی سریع</h2>
          <ul>
            <li><a href="/products/">محصولات</a></li>
            <li><a href="/services/">خدمات فنی</a></li>
            <li><a href="/articles/">دانشنامه</a></li>
            <li><a href="/about/">دربارهٔ شرکت</a></li>
            <li><a href="/faq/">پرسش‌های متداول</a></li>
            <li><a href="/contact/">تماس با ما</a></li>
          </ul>
        </nav>

        <nav class="footer-column" aria-label="دسته‌های تجهیزات">
          <h2>دسته‌های تجهیزات</h2>
          <ul>
            <li><a href="/products/?category=sample">آماده‌سازی نمونه</a></li>
            <li><a href="/products/?category=crushing">خردایش</a></li>
            <li><a href="/products/?category=grinding">آسیاکنی و پودرکنی</a></li>
            <li><a href="/products/?category=sizing">دانه‌بندی</a></li>
            <li><a href="/products/?category=separation">جدایش مواد معدنی</a></li>
          </ul>
        </nav>

        <div class="footer-contact">
          <h2>ارتباط با ما</h2>
          <p class="footer-address">
            <span class="footer-contact-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none"><path d="M19 10c0 5-7 11-7 11S5 15 5 10a7 7 0 1 1 14 0Z"/><circle cx="12" cy="10" r="2.3"/></svg></span>
            <span>تهران، شهرک صنعتی چهاردانگه، خیابان ۱۴، پلاک ۴</span>
          </p>
          <div class="footer-contact-cards">
            <a class="footer-contact-card" href="tel:+982155448318">
              <span class="footer-contact-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none"><path d="M7.2 3.5h2.6l1.4 4.1-1.8 1.6a14.4 14.4 0 0 0 5.4 5.4l1.6-1.8 4.1 1.4v2.6c0 1-.8 1.8-1.8 1.8A15.2 15.2 0 0 1 5.4 5.3c0-1 .8-1.8 1.8-1.8Z"/></svg></span>
              <span><small>تلفن دفتر</small><strong>۰۲۱ ۵۵۴۴ ۸۳۱۸</strong></span>
            </a>
            <a class="footer-contact-card" href="tel:+989006140897">
              <span class="footer-contact-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none"><path d="M7.5 3.5h9A2.5 2.5 0 0 1 19 6v12a2.5 2.5 0 0 1-2.5 2.5h-9A2.5 2.5 0 0 1 5 18V6a2.5 2.5 0 0 1 2.5-2.5Z"/><path d="M10 17.5h4"/></svg></span>
              <span><small>تلفن همراه</small><strong>۰۹۰۰ ۶۱۴ ۰۸۹۷</strong></span>
            </a>
            <a class="footer-contact-card" href="mailto:sales@chirehfg.com">
              <span class="footer-contact-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none"><rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="m4 7 8 6 8-6"/></svg></span>
              <span><small>واحد فروش</small><strong>sales@chirehfg.com</strong></span>
            </a>
            <a class="footer-contact-card" href="mailto:info@chirehfg.com">
              <span class="footer-contact-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none"><rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="m4 7 8 6 8-6"/></svg></span>
              <span><small>ایمیل شرکت</small><strong>info@chirehfg.com</strong></span>
            </a>
          </div>
        </div>
      </div>

      <div class="container footer-bottom">
        <span>© <span id="current-year">۲۰۲۶</span> چیره فرآور گستر. کلیهٔ حقوق محفوظ است.</span>
        <div class="footer-bottom-links">
          <a href="/privacy/">حریم خصوصی</a>
          <a href="https://chirehfg.com/" target="_blank" rel="noopener">وب‌سایت رسمی شرکت <span aria-hidden="true">↗</span></a>
        </div>
      </div>
    </footer>
    <a class="floating-call" href="tel:+982155448318" aria-label="تماس با چیره فرآور گستر"><span class="call-symbol" aria-hidden="true">☎</span><span>تماس با ما</span></a>
    '''

def layout(title, description, content, page_key="home", schema=None):
    full_title = title if "چیره فرآور گستر" in title else title + " | چیره فرآور گستر"
    schema_json = ""
    if schema:
        schema_json = '<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False).replace("</", "<\\/") + '</script>'
    return '''<!doctype html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#0b1c34">
<meta name="description" content="''' + esc(description) + '''">
<meta property="og:type" content="website">
<meta property="og:site_name" content="چیره فرآور گستر">
<meta property="og:title" content="''' + esc(full_title) + '''">
<meta property="og:description" content="''' + esc(description) + '''">
<meta property="og:image" content="/assets/mine.jpg">
<title>''' + esc(full_title) + '''</title>
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg" sizes="any">
<link rel="preload" href="/assets/vazirmatn.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css?v=footer-20261121b">
''' + schema_json + '''
</head>
<body data-page="''' + esc(page_key) + '''">
<a class="skip-link" href="#main-content">رفتن به محتوای اصلی</a>
''' + header() + '''
<main id="main-content">''' + content + '''</main>
''' + footer() + '''
<script src="/assets/site.js?v=menu-hover-2" defer></script>
</body>
</html>'''

def crumbs(items):
    out = ['<nav class="breadcrumbs container" aria-label="مسیر صفحه">']
    for idx, (label, href) in enumerate(items):
        if idx:
            out.append('<span aria-hidden="true" class="crumb-sep"></span>')
        if href:
            out.append('<a href="' + esc(href) + '">' + esc(label) + '</a>')
        else:
            out.append('<span aria-current="page">' + esc(label) + '</span>')
    out.append('</nav>')
    return "".join(out)

def write_page(path, title, description, content, page_key="home", schema=None):
    target = DIST / path / "index.html" if path else DIST / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(layout(title, description, content, page_key, schema), encoding="utf-8")

def specs_table(rows):
    return '<div class="spec-table-wrap"><table class="spec-table"><tbody>' + "".join(
        '<tr><th scope="row">' + esc(name) + '</th><td>' + esc(value) + '</td></tr>' for name, value in rows
    ) + '</tbody></table></div>'

def faq_list(items):
    return '<div class="faq-list">' + "".join(
        '<details class="faq-item"><summary>' + esc(question) + '</summary><div class="faq-answer"><p>' + esc(answer) + '</p></div></details>'
        for question, answer in items
    ) + '</div>'

def section_heading(kicker, title, copy="", align=""):
    return '<div class="section-heading ' + esc(align) + '"><span class="eyebrow">' + esc(kicker) + '</span><h2>' + title + '</h2>' + (('<p>' + copy + '</p>') if copy else '') + '</div>'

def article_card(article):
    return '<article class="article-card"><a class="article-visual article-' + esc(article["slug"]) + '" href="/articles/' + esc(article["slug"]) + '/"><span class="article-visual-label">' + esc(article["category"]) + '</span><span class="article-visual-mark" aria-hidden="true">CF</span></a><div class="article-card-body"><span class="article-category">' + esc(article["category"]) + '</span><h3><a href="/articles/' + esc(article["slug"]) + '/">' + esc(article["title"]) + '</a></h3><p>' + esc(article["summary"]) + '</p><a class="text-link" href="/articles/' + esc(article["slug"]) + '/">خواندن راهنما</a></div></article>'

# Home
featured_models = ["CRP-600", "CJC-200", "CSPI", "CST-L24"]
featured = [next(p for p in products if p["model"] == model) for model in featured_models]
home_content = '''
<section class="hero"><div class="hero-background" aria-hidden="true"></div><div class="container hero-grid">
  <div class="hero-copy"><span class="hero-kicker"><i></i> چیره فرآور گستر | تجهیزات فرآوری مواد معدنی</span>
    <h1>از نمونهٔ خام<br><em>تا دادهٔ قابل اتکا</em></h1>
    <p>تجهیزات آزمایشگاهی برای آماده‌سازی نمونه، خردایش، آسیاکنی، دانه‌بندی و جدایش مواد معدنی.</p>
    <div class="hero-actions"><a class="button button-primary" href="/products/">بررسی تجهیزات</a><a class="button button-outline-light" href="/contact/">گفت‌وگو با کارشناس</a></div>
    <div class="hero-proof"><span class="hero-proof-icon" aria-hidden="true"><svg viewBox="0 0 20 20"><path d="m3.5 10.5 4.2 4.2 8.8-9" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span>برای آزمایشگاه‌ها و فرآیندهای معدنی</span></div>
  </div>
  <div class="hero-visual"><div class="hero-orbit orbit-one"></div><div class="hero-orbit orbit-two"></div>
    <div class="hero-photo-label"><span class="photo-dot"></span><span>آماده‌سازی نمونه در مقیاس آزمایشگاهی</span></div>
    <img src="/assets/product_laboratory-pneumatic-ring-mill-crp-600.webp" alt="آسیاب رینگی پنوماتیکی آزمایشگاهی CRP-600" fetchpriority="high">
    <div class="hero-product-note"><span class="note-label">آسیاب رینگی پنوماتیکی</span><strong>CRP-600</strong><small>۶ مجموعهٔ مستقل هاون</small></div>
    <span class="hero-plus plus-a">+</span><span class="hero-plus plus-b">+</span>
  </div>
</div><div class="hero-bottom container"><span>فرآیند را از نقطهٔ درست آغاز کنید</span><span class="hero-line"></span><span>تجهیز متناسب با هدف آزمون</span></div></section>

<section class="process-strip"><div class="container process-grid">
  <a class="process-step" href="/products/?category=sample"><span class="process-symbol">نمونه</span><strong>آماده‌سازی</strong><small>تقسیم و آماده‌سازی نمونه</small></a>
  <span class="process-connector" aria-hidden="true"></span>
  <a class="process-step" href="/products/?category=crushing"><span class="process-symbol">خ</span><strong>خردایش</strong><small>کاهش ابعاد اولیه</small></a>
  <span class="process-connector" aria-hidden="true"></span>
  <a class="process-step" href="/products/?category=grinding"><span class="process-symbol">آ</span><strong>آسیاکنی</strong><small>نرمایش و پودرکردن</small></a>
  <span class="process-connector" aria-hidden="true"></span>
  <a class="process-step" href="/products/?category=separation"><span class="process-symbol">ج</span><strong>جدایش</strong><small>بررسی رفتار مادهٔ معدنی</small></a>
</div></section>

<section class="section section-products"><div class="container">
  ''' + section_heading("کاتالوگ منتخب", "تجهیز را بر اساس <span class=\"text-gradient\">مرحلهٔ فرآیند</span> پیدا کنید.", "چند نمونه از تجهیزات چیره فرآور گستر را ببینید و برای مشخصات کامل، وارد صفحهٔ محصول شوید.") + '''
  <div class="product-grid product-grid-home">''' + "".join(product_card(p, True) for p in featured) + '''</div>
  <div class="section-action"><a class="button button-dark" href="/products/">مشاهدهٔ همهٔ محصولات</a></div>
</div></section>

<section class="section section-showcase"><div class="container showcase-grid">
  <div class="showcase-copy"><span class="eyebrow eyebrow-light">مسیر انتخاب تجهیز</span><h2>هر آزمون، از یک پرسش فنی شروع می‌شود.</h2>
    <p>نوع نمونه، اندازهٔ خوراک و هدف آزمون روی انتخاب دستگاه اثر می‌گذارند. دسته‌های تجهیزات را مرحله‌به‌مرحله ببینید و مشخصات مدل‌ها را با نیاز آزمایشگاه مقایسه کنید.</p>
    <a class="button button-white" href="/services/">آشنایی با خدمات فنی</a>
  </div>
  <div class="showcase-steps">
    <div class="showcase-step"><span>الف</span><div><strong>ویژگی نمونه</strong><p>جنس، رطوبت و اندازهٔ خوراک را مشخص کنید.</p></div></div>
    <div class="showcase-step"><span>ب</span><div><strong>هدف آزمون</strong><p>خردایش، آسیاکنی، دانه‌بندی یا جدایش را تعیین کنید.</p></div></div>
    <div class="showcase-step"><span>پ</span><div><strong>بررسی مشخصات</strong><p>ظرفیت‌ها و شرایط کارکرد مدل‌ها را کنار هم بگذارید.</p></div></div>
  </div>
</div></section>

<section class="section section-light"><div class="container">
  ''' + section_heading("دانش فنی", "پیش از انتخاب دستگاه، <span class=\"text-gradient\">فرآیند را بشناسید.</span>", "راهنماهای کوتاه برای مقایسهٔ روش‌ها و تجهیزات آزمایشگاهی فرآوری مواد معدنی.") + '''
  <div class="article-grid">''' + "".join(article_card(a) for a in [
      {"slug":"sample-preparation","title":"آماده‌سازی نمونهٔ معدنی؛ از کجا شروع کنیم؟","category":"آماده‌سازی نمونه","summary":"مروری بر نقش کاهش ابعاد و تقسیم نمونه در طراحی یک مسیر آزمون روشن."},
      {"slug":"choosing-a-mill","title":"آسیاب رینگی یا گلوله‌ای؛ تفاوت در کاربرد چیست؟","category":"راهنمای انتخاب","summary":"مقایسهٔ دو خانوادهٔ آسیاب بر پایهٔ هدف آزمون، نوع نمونه و ظرفیت."},
      {"slug":"gravity-separation","title":"آشنایی با تجهیزات جدایش ثقلی آزمایشگاهی","category":"جدایش مواد معدنی","summary":"نگاهی به دو روش آزمایشگاهی و تفاوت میز لرزان با تغلیظ‌کنندهٔ گریز از مرکز."}
  ]) + '''</div>
  <div class="section-action"><a class="text-link" href="/articles/">رفتن به دانشنامه</a></div>
</div></section>

<section class="contact-band"><div class="container contact-band-inner"><div><span class="eyebrow">گام بعدی</span><h2>دربارهٔ نمونه و هدف آزمونتان بگویید.</h2><p>برای بررسی مشخصات و دریافت راهنمایی فنی، با چیره فرآور گستر در تماس باشید.</p></div><a class="button button-primary" href="/contact/">ثبت درخواست مشاوره</a></div></section>
'''
write_page("", "تجهیزات آزمایشگاهی فرآوری مواد معدنی", "چیره فرآور گستر؛ طراحی و ساخت تجهیزات آزمایشگاهی برای آماده‌سازی نمونه، خردایش، آسیاکنی، دانه‌بندی و جدایش مواد معدنی.", home_content, "home", organization_schema())

# Product catalog
filter_chips = [
    ("all", "همهٔ تجهیزات"), ("crushing", "خردایش"), ("grinding", "آسیاکنی"),
    ("sample", "آماده‌سازی نمونه"), ("sizing", "دانه‌بندی"), ("separation", "جدایش")
]
catalog_content = crumbs([("خانه", "/"), ("محصولات", None)]) + '''
<section class="page-hero page-hero-products"><div class="container page-hero-grid"><div><span class="eyebrow eyebrow-light">کاتالوگ تجهیزات</span><h1>محصولات چیره فرآور گستر</h1><p>تجهیزات را بر اساس مرحلهٔ فرآیند پیدا کنید؛ از خردایش و آسیاکنی تا جدایش و آماده‌سازی نمونه.</p></div><div class="page-hero-mark"><span>۲۴</span><small>تجهیز در کاتالوگ</small></div></div></section>
<section class="section"><div class="container">
  <div class="catalog-toolbar"><label class="search-box"><span class="search-icon" aria-hidden="true"></span><span class="visually-hidden">جست‌وجو در تجهیزات</span><input type="search" id="product-search" placeholder="نام یا مدل دستگاه را جست‌وجو کنید" autocomplete="off"></label><p class="catalog-count" id="catalog-count">در حال نمایش محصولات</p></div>
  <div class="filter-chips" role="group" aria-label="فیلتر دسته‌بندی محصولات">''' + "".join(
      '<button type="button" class="filter-chip' + (' is-active' if key=="all" else '') + '" data-filter="' + key + '" aria-pressed="' + ('true' if key=="all" else 'false') + '">' + label + '</button>'
      for key,label in filter_chips
  ) + '''</div>
  <div class="product-grid catalog-grid" id="product-grid">''' + "".join(product_card(p) for p in products) + '''</div>
  <p class="empty-state" id="empty-products" hidden>محصولی با این عبارت پیدا نشد. عبارت دیگری را جست‌وجو کنید.</p>
</div></section>
'''
write_page("products", "محصولات و تجهیزات فرآوری", "کاتالوگ تجهیزات آزمایشگاهی فرآوری مواد معدنی چیره فرآور گستر؛ جست‌وجو و فیلتر دستگاه‌ها بر اساس مرحلهٔ فرآیند.", catalog_content, "products")

# Product details
for model, detail in DETAILS.items():
    prod = next((p for p in products if p["model"] == model), None)
    faq = faq_list(detail["faqs"])
    features = "".join('<li><span class="check-mark" aria-hidden="true"></span>' + esc(item) + '</li>' for item in detail["features"])
    image = detail["image"]
    specs = specs_table(detail["specs"])
    related = [p for p in products if p["model"] in ["CRP-600", "CJC-200", "CSPI", "CBM", "CST-L24", "CCG-L40"] and p["model"] != model][:3]
    related_cards = "".join(product_card(p, True) for p in related)
    content = crumbs([("خانه", "/"), ("محصولات", "/products/"), (detail["title"], None)]) + '''
    <section class="product-detail-hero"><div class="container product-detail-grid">
      <div class="product-detail-copy"><span class="eyebrow">''' + esc(detail["category"]) + '''</span>
        <p class="product-detail-code">''' + esc(model) + '''</p><h1>''' + esc(detail["title"]) + '''</h1><p class="lead">''' + esc(detail["intro"]) + '''</p>
        <div class="product-detail-actions"><a class="button button-primary" href="/contact/?product=''' + __import__("urllib.parse").parse.quote(detail["title"]) + '''">درخواست مشاوره و استعلام</a><a class="button button-outline-dark" href="#specs">مشاهدهٔ مشخصات فنی</a></div>
        <div class="product-detail-mini"><span>اطلاعات فنی بر اساس کاتالوگ محصول</span><span>پیکربندی نهایی با کارشناس بررسی می‌شود</span></div>
      </div><figure class="product-detail-visual"><div class="product-image-glow"></div><img src="/assets/''' + esc(image) + '''" alt="''' + esc(detail["title"]) + '''" fetchpriority="high"><figcaption>تصویر محصول از وب‌سایت چیره فرآور گستر</figcaption></figure>
    </div></section>
    <nav class="product-tabs container" aria-label="بخش‌های صفحهٔ محصول"><a href="#overview">معرفی محصول</a><a href="#features">ویژگی‌ها</a><a href="#specs">مشخصات فنی</a><a href="#questions">پرسش‌ها</a></nav>
    <section class="section product-overview" id="overview"><div class="container detail-copy-grid"><div>''' + section_heading("معرفی محصول", "طراحی‌شده برای نیاز مشخص آزمایشگاه") + '''</div><div class="long-copy">''' + "".join("<p>" + esc(p) + "</p>" for p in detail["paragraphs"]) + '''</div></div></section>
    <section class="section section-light" id="features"><div class="container feature-section-grid"><div>''' + section_heading("ویژگی‌ها", "جزئیاتی که در انتخاب اهمیت دارند.") + '''</div><ul class="feature-list">''' + features + '''</ul></div></section>
    <section class="section" id="specs"><div class="container specs-section-grid"><div>''' + section_heading("جدول مشخصات", "اطلاعات فنی ''' + esc(model) + '''", "برای بررسی تناسب دستگاه با نمونه و شرایط نصب، مشخصات را با کارشناس فنی تطبیق دهید.") + '''<a class="text-link" href="/contact/?product=''' + __import__("urllib.parse").parse.quote(detail["title"]) + '''">پرسش دربارهٔ این محصول</a></div><div>''' + specs + '''<p class="spec-note">ظرفیت‌ها و نتایج عملیاتی ممکن است با توجه به ویژگی نمونه و شرایط آزمون تغییر کنند. مشخصات نهایی را پیش از سفارش از شرکت استعلام کنید.</p></div></div></section>
    <section class="section section-light" id="questions"><div class="container faq-section-grid"><div>''' + section_heading("پرسش‌های محصول", "پاسخ‌های کوتاه دربارهٔ ''' + esc(model) + '''") + '''</div><div>''' + faq + '''</div></div></section>
    <section class="section"><div class="container">''' + section_heading("تجهیزات مرتبط", "مدل‌های دیگری برای مقایسه") + '''<div class="product-grid product-grid-home">''' + related_cards + '''</div></div></section>
    <section class="contact-band"><div class="container contact-band-inner"><div><span class="eyebrow">بررسی فنی</span><h2>برای انتخاب پیکربندی مناسب، مشاوره بگیرید.</h2><p>نوع ماده، اندازهٔ خوراک و هدف آزمون را با کارشناسان چیره فرآور گستر مطرح کنید.</p></div><a class="button button-primary" href="/contact/?product=''' + __import__("urllib.parse").parse.quote(detail["title"]) + '''">درخواست مشاوره</a></div></section>
    '''
    write_page("products/" + detail["slug"], detail["title"], detail["intro"], content, "product", product_schema(detail))

# About
about_content = crumbs([("خانه", "/"), ("دربارهٔ ما", None)]) + '''
<section class="page-hero page-hero-about"><div class="container page-hero-grid"><div><span class="eyebrow eyebrow-light">دربارهٔ شرکت</span><h1>تجهیزات دقیق برای<br>پرسش‌های واقعی فرآوری</h1><p>چیره فرآور گستر در زمینهٔ طراحی و ساخت تجهیزات آزمایشگاهی فرآوری مواد معدنی فعالیت می‌کند.</p></div><div class="about-mark"><span>چیره</span><small>فرآور گستر</small></div></div></section>
<section class="section"><div class="container about-intro-grid"><div>''' + section_heading("شناخت شرکت", "از نیاز آزمایشگاه تا طراحی تجهیز") + '''</div><div class="long-copy"><p>تخصص چیره فرآور گستر، تولید تجهیزاتی است که در مراحل آماده‌سازی نمونه، خردایش، آسیاکنی، دانه‌بندی و جدایش مواد معدنی در آزمایشگاه‌ها و واحدهای فرآوری به‌کار می‌روند.</p><p>در معرفی هر دستگاه، ظرفیت، ابعاد خوراک و شرایط کارکرد اهمیت دارند. این مشخصات کمک می‌کنند تجهیز با هدف آزمون و امکانات محل استفاده سنجیده شود.</p><p>برای بررسی مدل‌ها، دریافت مشخصات فنی یا گفت‌وگو دربارهٔ نیاز فرآیند، می‌توانید با واحد فروش و مهندسی شرکت تماس بگیرید.</p></div></div></section>
<section class="about-image-section"><div class="container about-image-grid"><div class="about-image"><img src="/assets/industry.jpg" alt="نمایی از محیط صنعتی و تجهیزات فرآوری مواد معدنی" loading="lazy"><span class="image-caption">فضای صنعتی فرآوری مواد معدنی</span></div><div class="about-image-copy"><span class="eyebrow eyebrow-light">حوزهٔ فعالیت</span><h2>تجهیزات در خدمت زنجیرهٔ آماده‌سازی و آزمون</h2><p>محصولات شرکت طیفی از سنگ‌شکن و آسیاب تا تجهیزات نمونه‌برداری، طبقه‌بندی و جدایش را در بر می‌گیرند. کاتالوگ هر دستگاه، اطلاعات فنی همان مدل را ارائه می‌کند.</p><a class="button button-white" href="/products/">مرور محصولات</a></div></div></section>
<section class="section"><div class="container">''' + section_heading("مسیر فرآیند", "چهار مرحله؛ یک نگاه منسجم") + '''
  <div class="about-process-grid">
    <div><span class="process-symbol">الف</span><h3>آماده‌سازی نمونه</h3><p>تقسیم نمونه و آماده‌کردن آن برای آزمون.</p></div>
    <div><span class="process-symbol">ب</span><h3>خردایش</h3><p>کاهش ابعاد اولیه با سنگ‌شکن‌های آزمایشگاهی.</p></div>
    <div><span class="process-symbol">پ</span><h3>آسیاکنی</h3><p>نرمایش یا پودرکردن متناسب با هدف آزمایش.</p></div>
    <div><span class="process-symbol">ت</span><h3>جدایش</h3><p>بررسی رفتار نمونه در روش‌های جدایش آزمایشگاهی.</p></div>
  </div>
</div></section>
<section class="contact-band"><div class="container contact-band-inner"><div><span class="eyebrow">ارتباط با چیره</span><h2>دربارهٔ تجهیز موردنیازتان صحبت کنیم.</h2><p>راه‌های تماس و فرم درخواست مشاوره در دسترس شماست.</p></div><a class="button button-primary" href="/contact/">تماس با شرکت</a></div></section>
'''
write_page("about", "دربارهٔ چیره فرآور گستر", "آشنایی با چیره فرآور گستر، زمینهٔ فعالیت و تجهیزات آزمایشگاهی فرآوری مواد معدنی.", about_content, "about", organization_schema())

# Services
services_content = crumbs([("خانه", "/"), ("خدمات", None)]) + '''
<section class="page-hero page-hero-services"><div class="container page-hero-grid"><div><span class="eyebrow eyebrow-light">خدمات فنی</span><h1>از انتخاب تجهیز<br>تا راه‌اندازی</h1><p>برای شناخت مدل‌ها، بررسی مشخصات و هماهنگی خدمات مرتبط با دستگاه، با تیم چیره فرآور گستر گفت‌وگو کنید.</p></div><div class="page-hero-mark"><span>فنی</span><small>مشاوره و پاسخ‌گویی</small></div></div></section>
<section class="section"><div class="container">''' + section_heading("همراهی فنی", "خدمت از نیاز واقعی شما آغاز می‌شود.", "نوع نمونه، هدف آزمون و شرایط محل استفاده، نقطهٔ شروع یک گفت‌وگوی فنی هستند.") + '''
  <div class="service-grid">
    <article class="service-card"><span class="service-icon">مشاوره</span><h3>راهنمای انتخاب دستگاه</h3><p>مشخصات نمونه و هدف آزمایش را مطرح کنید تا مدل‌ها و پارامترهای فنی مرتبط بررسی شوند.</p><a class="text-link" href="/contact/?subject=مشاوره%20فنی">درخواست مشاوره</a></article>
    <article class="service-card"><span class="service-icon">ساخت</span><h3>طراحی و ساخت تجهیزات</h3><p>چیره فرآور گستر در زمینهٔ طراحی و ساخت تجهیزات آزمایشگاهی فرآوری مواد معدنی فعالیت می‌کند.</p><a class="text-link" href="/products/">مشاهدهٔ محصولات</a></article>
    <article class="service-card"><span class="service-icon">پشتیبانی</span><h3>هماهنگی فنی و پیگیری سفارش</h3><p>برای دریافت اطلاعات فنی هر مدل یا پیگیری درخواست، از طریق تلفن، ایمیل یا فرم تماس ارتباط بگیرید.</p><a class="text-link" href="/contact/">راه‌های ارتباطی</a></article>
  </div>
</div></section>
<section class="section section-dark"><div class="container"><div class="section-heading section-heading-light"><span class="eyebrow eyebrow-light">مسیر همکاری</span><h2>درخواست را روشن و مرحله‌به‌مرحله پیش ببریم.</h2></div>
  <div class="service-steps"><div><span>۱</span><h3>شرح نیاز</h3><p>نوع ماده و هدف آزمون را مطرح کنید.</p></div><div><span>۲</span><h3>بررسی مشخصات</h3><p>مدل‌ها و پارامترهای فنی مرتبط را مرور کنید.</p></div><div><span>۳</span><h3>هماهنگی</h3><p>برای استعلام یا پیگیری سفارش با شرکت در تماس باشید.</p></div></div>
</div></section>
'''
write_page("services", "خدمات فنی و مشاوره", "خدمات فنی چیره فرآور گستر برای بررسی مشخصات تجهیزات آزمایشگاهی فرآوری مواد معدنی، انتخاب دستگاه و هماهنگی سفارش.", services_content, "services")

# FAQ
general_faqs = [
    ["چطور دستگاه مناسب را انتخاب کنم؟", "نوع نمونه، اندازهٔ خوراک، هدف آزمون، ظرفیت موردنیاز و شرایط نصب را مشخص کنید. سپس مشخصات مدل‌ها را با کارشناس فنی بررسی کنید."],
    ["چیره فرآور گستر چه تجهیزاتی تولید می‌کند؟", "محصولات شرکت شامل تجهیزات خردایش، آسیاکنی، آماده‌سازی نمونه، دانه‌بندی و جدایش مواد معدنی است."],
    ["آیا برای محصولات مشخصات فنی در دسترس است؟", "بله؛ در صفحهٔ هر مدل، مشخصات موجود مانند ابعاد خوراک، ظرفیت برآوردی، توان و شرایط کارکرد درج شده است."],
    ["برای قیمت و زمان تحویل چطور استعلام بگیرم؟", "با شمارهٔ ۰۲۱ ۵۵۴۴ ۸۳۱۸ تماس بگیرید یا فرم تماس را تکمیل کنید تا درخواست از طریق ایمیل برای شرکت آماده شود."],
    ["آیا مشخصات ظرفیت همیشه در عمل ثابت است؟", "خیر؛ ظرفیت‌های اعلام‌شده به مدل و شرایط آزمون وابسته‌اند. نوع ماده، دانه‌بندی و تنظیم دستگاه می‌توانند بر نتیجه اثر بگذارند."],
    ["برای مشاورهٔ فنی چه اطلاعاتی آماده کنم؟", "نام ماده، دانه‌بندی و رطوبت تقریبی، هدف آزمون و ظرفیت موردنیاز را آماده کنید. هر اطلاعاتی که در دسترس نیست را هم در درخواست بنویسید."]
]
faq_content = crumbs([("خانه", "/"), ("پرسش‌های متداول", None)]) + '''
<section class="page-hero page-hero-faq"><div class="container page-hero-grid"><div><span class="eyebrow eyebrow-light">پاسخ‌گویی</span><h1>پرسش‌های متداول</h1><p>پاسخ به پرسش‌های اولیه دربارهٔ انتخاب تجهیزات، مشخصات فنی و راه‌های ارتباط با چیره فرآور گستر.</p></div><div class="page-hero-mark"><span>؟</span><small>پرسش و پاسخ</small></div></div></section>
<section class="section"><div class="container faq-page-grid"><div>''' + section_heading("راهنمای سریع", "پاسخ کوتاه، تصمیم روشن‌تر") + '''<p class="long-copy">برای بررسی دقیق‌تر یک مدل یا شرایط خاص نمونه، با واحد فروش و مهندسی چیره فرآور گستر تماس بگیرید.</p><a class="button button-dark" href="/contact/">پرسش از کارشناس</a></div><div>''' + faq_list(general_faqs) + '''</div></div></section>
'''
write_page("faq", "پرسش‌های متداول", "پاسخ پرسش‌های متداول دربارهٔ انتخاب و مشخصات تجهیزات آزمایشگاهی فرآوری مواد معدنی چیره فرآور گستر.", faq_content, "faq")

# Privacy notice for the prototype's email-based contact form.
privacy_content = crumbs([("خانه", "/"), ("حریم خصوصی", None)]) + '''
<section class="page-hero page-hero-faq"><div class="container page-hero-grid"><div><span class="eyebrow eyebrow-light">اطلاع‌رسانی</span><h1>حریم خصوصی</h1><p>نحوهٔ استفاده از اطلاعاتی که برای تماس یا درخواست مشاوره وارد می‌کنید.</p></div><div class="page-hero-mark"><span>امن</span><small>اطلاع از روند درخواست</small></div></div></section>
<section class="section"><div class="container article-body privacy-body"><section><h2>فرم تماس در این نمونه‌کار</h2><p>فرم تماس این نسخه، اطلاعات واردشده را در وب‌سایت ذخیره نمی‌کند. پس از تکمیل فرم، نرم‌افزار ایمیل شما با متن آماده باز می‌شود و ارسال پیام فقط پس از تأیید شما در همان نرم‌افزار انجام خواهد شد.</p></section><section><h2>اطلاعات تماس شرکت</h2><p>پیام‌های ایمیلی به نشانی فروش شرکت ارسال می‌شوند. پیش از ارسال، نشانی و متن پیام را در برنامهٔ ایمیل خود بررسی کنید.</p><p>برای ارتباط مستقیم می‌توانید از شماره‌های درج‌شده در صفحهٔ تماس استفاده کنید.</p></section><section><h2>نسخهٔ عملیاتی وب‌سایت</h2><p>اگر این طرح برای وب‌سایت اصلی پیاده‌سازی شود و فرم به سامانهٔ ثبت درخواست متصل گردد، متن این صفحه باید با شیوهٔ واقعی جمع‌آوری، نگهداری و دسترسی به اطلاعات هماهنگ شود.</p></section></div></section>
'''
write_page("privacy", "حریم خصوصی", "اطلاع دربارهٔ نحوهٔ آماده‌سازی و ارسال پیام در فرم تماس نمونه‌کار چیره فرآور گستر.", privacy_content, "privacy")

# Contact
contact_content = crumbs([("خانه", "/"), ("تماس با ما", None)]) + '''
<section class="page-hero page-hero-contact"><div class="container page-hero-grid"><div><span class="eyebrow eyebrow-light">ارتباط مستقیم</span><h1>بیایید دربارهٔ<br>نیاز فرآیند صحبت کنیم.</h1><p>برای مشاوره، استعلام قیمت یا پیگیری سفارش از راه‌های زیر با چیره فرآور گستر تماس بگیرید.</p></div><div class="contact-hero-card"><span>پاسخ‌گویی تلفنی</span><a href="tel:+982155448318">۰۲۱ ۵۵۴۴ ۸۳۱۸</a><small>برای درخواست فنی و استعلام محصول</small></div></div></section>
<section class="section"><div class="container contact-page-grid">
  <div class="contact-info"><span class="eyebrow">راه‌های ارتباطی</span><h2>در دسترس شما هستیم.</h2><p>برای اینکه درخواست شما دقیق‌تر بررسی شود، مدل دستگاه یا هدف آزمون را در پیام خود بنویسید.</p>
    <a class="contact-method" href="tel:+982155448318"><span class="contact-method-icon">تلفن</span><span><strong>۰۲۱ ۵۵۴۴ ۸۳۱۸</strong><small>تماس با دفتر شرکت</small></span></a>
    <a class="contact-method" href="tel:+989006140897"><span class="contact-method-icon">موبایل</span><span><strong>۰۹۰۰ ۶۱۴ ۰۸۹۷</strong><small>تماس مستقیم</small></span></a>
    <a class="contact-method" href="mailto:sales@chirehfg.com"><span class="contact-method-icon">ایمیل</span><span><strong>sales@chirehfg.com</strong><small>درخواست فروش و استعلام</small></span></a>
    <a class="contact-method" href="mailto:info@chirehfg.com"><span class="contact-method-icon">ایمیل</span><span><strong>info@chirehfg.com</strong><small>ارتباط عمومی</small></span></a>
    <div class="address-card"><span class="address-label">نشانی</span><p>تهران، شهرک صنعتی چهاردانگه، خیابان ۱۴، پلاک ۴</p><a class="text-link" href="https://maps.google.com/?q=%D8%B4%D9%87%D8%B1%DA%A9+%D8%B5%D9%86%D8%B9%D8%AA%DB%8C+%DA%86%D9%87%D8%A7%D8%B1%D8%AF%D8%A7%D9%86%DA%AF%D9%87+%D8%AE%DB%8C%D8%A7%D8%A8%D8%A7%D9%86+%DB%B1%DB%B4+%D9%BE%D9%84%D8%A7%DA%A9+%DB%B4" target="_blank" rel="noopener">نمایش نشانی در نقشه</a></div>
  </div>
  <div class="contact-form-card"><span class="eyebrow">ارسال درخواست</span><h2>درخواستتان را بنویسید.</h2><p>فرم، پیام را در نرم‌افزار ایمیل شما آماده می‌کند.</p>
    <form id="contact-form">
      <label>نام و نام خانوادگی<input name="name" type="text" autocomplete="name" required placeholder="نام شما"></label>
      <div class="form-row"><label>شمارهٔ تماس<input name="phone" type="tel" autocomplete="tel" required placeholder="مثلاً ۰۹۱۲۱۲۳۴۵۶۷"></label><label>ایمیل <span>(اختیاری)</span><input name="email" type="email" autocomplete="email" placeholder="name@example.com"></label></div>
      <label>موضوع درخواست<select name="subject" id="contact-subject"><option value="مشاوره و استعلام تجهیزات">مشاوره و استعلام تجهیزات</option><option value="پیگیری سفارش">پیگیری سفارش</option><option value="اطلاعات فنی محصول">اطلاعات فنی محصول</option><option value="سایر درخواست‌ها">سایر درخواست‌ها</option></select></label>
      <label>محصول موردنظر <span>(اختیاری)</span><input name="product" id="contact-product" type="text" placeholder="نام یا مدل دستگاه"></label>
      <label>پیام<textarea name="message" rows="5" required placeholder="نوع نمونه و هدف آزمون را توضیح دهید."></textarea></label>
      <button class="button button-primary form-submit" type="submit">آماده‌سازی پیام ایمیل</button>
      <p class="form-note" id="form-status" role="status">پس از فشردن دکمه، نرم‌افزار ایمیل شما برای ارسال پیام باز می‌شود.</p>
    </form>
  </div>
</div></section>
'''
write_page("contact", "تماس و درخواست مشاوره", "راه‌های تماس با چیره فرآور گستر برای مشاوره، استعلام قیمت یا پیگیری سفارش تجهیزات آزمایشگاهی فرآوری مواد معدنی.", contact_content, "contact")

# Editorial pages
articles = [
    {
        "slug": "sample-preparation",
        "title": "آماده‌سازی نمونهٔ معدنی؛ از کجا شروع کنیم؟",
        "category": "آماده‌سازی نمونه",
        "summary": "مروری بر نقش کاهش ابعاد و تقسیم نمونه در طراحی یک مسیر آزمون روشن.",
        "intro": "پیش از انتخاب دستگاه، باید روشن باشد چه پرسشی از نمونه می‌خواهیم پاسخ دهیم. آماده‌سازی نمونه بخشی از همین مسیر است: نمونه باید برای آزمون موردنظر به شکل و اندازهٔ مناسب برسد.",
        "sections": [
            ("از هدف آزمون آغاز کنید", ["هدف آزمون تعیین می‌کند که نمونه به چه دانه‌بندی و مقداری نیاز دارد. بنابراین بهتر است پیش از انتخاب تجهیز، کاربرد نهایی نمونه و روش اندازه‌گیری مشخص باشد."]),
            ("کاهش ابعاد و تقسیم نمونه", ["در بسیاری از مسیرها، کاهش ابعاد با خردایش اولیه آغاز می‌شود و سپس نمونه برای مراحل بعدی آماده می‌شود. اگر بخشی از نمونه باید جداگانه بررسی شود، تقسیم نمونه نیز در مسیر قرار می‌گیرد.", "سنگ‌شکن فکی CJC-200 برای خردایش اولیه و تقسیم‌کن‌های شانه‌ای سری CWR و CSR برای تقسیم نمونه در فهرست تجهیزات چیره فرآور گستر قرار دارند."]),
            ("مشخصات را با شرایط نمونه تطبیق دهید", ["اندازهٔ خوراک، رطوبت، جنس ماده و مقدار نمونه بر انتخاب دستگاه اثر دارند. ارقام ظرفیت و دانه‌بندی هر مدل را در کنار این شرایط بخوانید و برای موارد خاص از کارشناس فنی راهنمایی بگیرید."])
        ]
    },
    {
        "slug": "choosing-a-mill",
        "title": "آسیاب رینگی یا گلوله‌ای؛ تفاوت در کاربرد چیست؟",
        "category": "راهنمای انتخاب",
        "summary": "مقایسهٔ دو خانوادهٔ آسیاب بر پایهٔ هدف آزمون، نوع نمونه و ظرفیت.",
        "intro": "آسیاب رینگی و آسیاب گلوله‌ای هر دو برای کاهش ابعاد نمونه به‌کار می‌روند، اما ساختار و شیوهٔ استفادهٔ آن‌ها یکسان نیست. انتخاب به هدف آزمایش و مشخصات نمونه بستگی دارد.",
        "sections": [
            ("آسیاب رینگی CRP-600", ["CRP-600 شش مجموعهٔ هاون مستقل ۱۰۰ میلی‌لیتری دارد و برای پودرکردن هم‌زمان چند نمونه طراحی شده است. خوراک پیشنهادی کمتر از ۲ میلی‌متر است و دانه‌بندی کمتر از ۷۵ میکرون در شرایط مناسب قابل دستیابی است."]),
            ("آسیاب گلوله‌ای سری CBM", ["سری CBM در چهار مدل عرضه می‌شود و برای آسیاکنی خشک یا تر به‌صورت ناپیوسته قابل استفاده است. ظرفیت برآوردی مواد خشک از ۱ تا ۹ کیلوگرم در هر نوبت، بسته به مدل، متغیر است."]),
            ("کدام را بررسی کنیم؟", ["اگر تعداد نمونه‌های مستقل و آماده‌سازی هم‌زمان اهمیت دارد، ساختار چندهاونهٔ CRP-600 را بررسی کنید. اگر آزمون ناپیوستهٔ خشک یا تر و ظرفیت متناسب با مدل مدنظر است، مشخصات سری CBM را مقایسه کنید. برای انتخاب نهایی، اندازهٔ خوراک و هدف آزمون را نیز در نظر بگیرید."])
        ]
    },
    {
        "slug": "gravity-separation",
        "title": "آشنایی با تجهیزات جدایش ثقلی آزمایشگاهی",
        "category": "جدایش مواد معدنی",
        "summary": "نگاهی به دو روش آزمایشگاهی و تفاوت میز لرزان با تغلیظ‌کنندهٔ گریز از مرکز.",
        "intro": "تجهیزات جدایش ثقلی در مقیاس آزمایشگاهی برای بررسی رفتار نمونه و مطالعهٔ شرایط فرآیند به‌کار می‌روند. دو نمونه از محصولات چیره فرآور گستر، میز لرزان CST-L24 و تغلیظ‌کنندهٔ گریز از مرکز CCG-L40 هستند.",
        "sections": [
            ("میز لرزان CST-L24", ["CST-L24 با مکانیزم ویلفلی مدل B13، حرکت رفت‌وبرگشتی صفحه را با جریان عرضی آب ترکیب می‌کند. صفحهٔ فایبرگلاس، تنظیم مستقل شیب و جمع‌آوری سه محصول از ویژگی‌های این مدل است."]),
            ("تغلیظ‌کنندهٔ گریز از مرکز CCG-L40", ["CCG-L40 برای آزمون نیمه‌پیوستهٔ جدایش ثقلی در مقیاس آزمایشگاهی طراحی شده است. محدودهٔ دانه‌بندی خوراک ۱۰ تا ۵۰۰ میکرومتر و محدودهٔ شتاب گریز از مرکز صفر تا ۲۰۰ G اعلام شده است."]),
            ("مقایسهٔ شرایط آزمون", ["این دو تجهیز از سازوکارهای متفاوتی استفاده می‌کنند؛ بنابراین نوع نمونه، دانه‌بندی و هدف جدایش در انتخاب اهمیت دارند. مشخصات و ظرفیت اعلام‌شده را با شرایط واقعی آزمایشگاه تطبیق دهید."])
        ]
    }
]

def article_card(article):
    return '<article class="article-card"><a class="article-visual article-' + esc(article["slug"]) + '" href="/articles/' + esc(article["slug"]) + '/"><span class="article-visual-label">' + esc(article["category"]) + '</span><span class="article-visual-mark" aria-hidden="true">CF</span></a><div class="article-card-body"><span class="article-category">' + esc(article["category"]) + '</span><h3><a href="/articles/' + esc(article["slug"]) + '/">' + esc(article["title"]) + '</a></h3><p>' + esc(article["summary"]) + '</p><a class="text-link" href="/articles/' + esc(article["slug"]) + '/">خواندن راهنما</a></div></article>'

articles_content = crumbs([("خانه", "/"), ("دانشنامه", None)]) + '''
<section class="page-hero page-hero-articles"><div class="container page-hero-grid"><div><span class="eyebrow eyebrow-light">دانشنامهٔ فرآوری</span><h1>برای انتخاب،<br>یک قدم آگاهانه‌تر.</h1><p>راهنماهای فنی کوتاه دربارهٔ آماده‌سازی نمونه و تجهیزات فرآوری مواد معدنی.</p></div><div class="page-hero-mark"><span>دانش</span><small>راهنمای تجهیزات و فرآیند</small></div></div></section>
<section class="section"><div class="container">''' + section_heading("مقاله‌ها", "موضوع را انتخاب کنید.", "راهنمای هر مطلب به یک پرسش فنی مشخص می‌پردازد.") + '<div class="article-grid">' + "".join(article_card(a) for a in articles) + '</div></div></section>'
write_page("articles", "دانشنامهٔ فرآوری مواد معدنی", "راهنماهای چیره فرآور گستر دربارهٔ آماده‌سازی نمونه، انتخاب آسیاب آزمایشگاهی و تجهیزات جدایش ثقلی.", articles_content, "articles")

for article in articles:
    sections = "".join('<section><h2>' + esc(head) + '</h2>' + "".join('<p>' + esc(text) + '</p>' for text in paragraphs) + '</section>' for head, paragraphs in article["sections"])
    article_schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": article["title"],
        "description": article["summary"],
        "publisher": {"@type": "Organization", "name": "چیره فرآور گستر"}
    }
    content = crumbs([("خانه", "/"), ("دانشنامه", "/articles/"), (article["title"], None)]) + '''
    <article class="article-page"><header class="article-page-header"><span class="eyebrow">''' + esc(article["category"]) + '''</span><h1>''' + esc(article["title"]) + '''</h1><p class="lead">''' + esc(article["intro"]) + '''</p><div class="article-meta"><span>راهنمای فنی چیره فرآور گستر</span><span>مطالعهٔ کوتاه</span></div></header>
    <div class="article-page-image article-''' + esc(article["slug"]) + '''"><span class="article-visual-label">''' + esc(article["category"]) + '''</span></div>
    <div class="article-body">''' + sections + '''<aside class="article-callout"><strong>برای شرایط نمونهٔ خودتان راهنمایی می‌خواهید؟</strong><p>مدل دستگاه و هدف آزمون را با کارشناسان چیره فرآور گستر مطرح کنید.</p><a class="button button-dark" href="/contact/">درخواست مشاوره</a></aside></div>
    </article>
    '''
    write_page("articles/" + article["slug"], article["title"], article["summary"], content, "article", article_schema)

# 404
not_found = '<section class="not-found"><div class="container"><span class="eyebrow">صفحه پیدا نشد</span><h1>این مسیر در دسترس نیست.</h1><p>از فهرست تجهیزات یا صفحهٔ اصلی ادامه دهید.</p><div class="hero-actions"><a class="button button-primary" href="/">بازگشت به خانه</a><a class="button button-outline-dark" href="/products/">مرور محصولات</a></div></div></section>'
write_page("404", "صفحه پیدا نشد", "صفحهٔ موردنظر در وب‌سایت چیره فرآور گستر پیدا نشد.", not_found, "not-found")
shutil.copy2(DIST / "404" / "index.html", DIST / "404.html")

CSS = r"""
@font-face{font-family:Vazirmatn;src:url('/assets/vazirmatn.woff2') format('woff2');font-style:normal;font-weight:100 900;font-display:swap}
:root{--navy:#0b1c34;--navy-2:#112846;--blue:#1971d4;--blue-2:#2f8ae9;--cyan:#71d7e3;--orange:#f5a45d;--ink:#13263e;--muted:#63748a;--line:#dce5ef;--cloud:#f2f6fb;--white:#fff;--shadow:0 22px 60px rgba(13,36,65,.12);--radius:22px;--max:1200px}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:100px}
body{margin:0;background:var(--white);color:var(--ink);font-family:Vazirmatn,Tahoma,sans-serif;font-size:16px;line-height:1.85;text-rendering:optimizeLegibility}
img{display:block;max-width:100%}
a{color:inherit;text-decoration:none}
button,input,select,textarea{font:inherit}
button,a,input,select,textarea{-webkit-tap-highlight-color:transparent}
button:focus-visible,a:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible,summary:focus-visible{outline:3px solid rgba(25,113,212,.38);outline-offset:3px}
::selection{background:rgba(25,113,212,.2)}
.container{width:min(var(--max),calc(100% - 48px));margin-inline:auto}
.skip-link{position:absolute;top:8px;right:8px;z-index:200;transform:translateY(-150%);background:#fff;color:var(--navy);padding:8px 14px;border-radius:8px}
.skip-link:focus{transform:translateY(0)}
.utility-bar{background:#071529;color:#d2deec;font-size:14px}
.utility-inner{height:38px;display:flex;align-items:center;justify-content:space-between}
.utility-links{display:flex;align-items:center;gap:16px;color:#f4f7fb}
.utility-links a:hover{color:var(--cyan)}
.utility-separator{width:1px;height:15px;background:rgba(255,255,255,.25)}
.site-header{height:88px;position:sticky;top:0;z-index:50;background:rgba(255,255,255,.96);backdrop-filter:blur(16px);border-bottom:1px solid rgba(220,229,239,.8)}
.header-inner{height:100%;display:flex;align-items:center;gap:32px}
.brand{display:flex;align-items:center;gap:10px;flex:0 0 auto}
.brand-mark{width:42px;height:42px;display:grid;place-items:center;color:var(--blue)}
.brand-mark svg{width:100%;height:100%}
.brand-copy{display:flex;flex-direction:column;line-height:1.45}
.brand-copy strong{font-size:17px;font-weight:800;color:var(--navy)}
.brand-copy small{font-size:12px;color:var(--muted)}
.primary-nav{display:flex;align-items:center;gap:25px;margin-inline-start:auto;height:100%;font-size:15px;color:#2d4058}
.primary-nav>a,.nav-products>summary{height:100%;display:flex;align-items:center;position:relative;cursor:pointer;list-style:none;white-space:nowrap}
.primary-nav>a::after,.nav-products>summary::after{content:"";height:2px;background:var(--blue);position:absolute;bottom:20px;right:0;left:100%;transition:left .25s}
.primary-nav>a:hover::after,.primary-nav>a[aria-current=page]::after,.nav-products>summary:hover::after,.nav-products[open]>summary::after{left:0}
.nav-products{height:100%;position:relative}
.nav-products>summary::-webkit-details-marker{display:none}
.nav-products>summary:after{content:"";width:7px;height:7px;border-inline-start:1.5px solid currentColor;border-bottom:1.5px solid currentColor;transform:rotate(-45deg);margin-inline-start:8px;margin-top:-4px}
.mega-menu{position:absolute;top:calc(100% - 5px);right:-90px;width:min(650px,90vw);padding:24px;background:#fff;box-shadow:var(--shadow);border:1px solid var(--line);border-radius:18px;display:grid;grid-template-columns:.9fr 1.6fr;gap:22px}
.mega-intro{padding:17px;background:var(--cloud);border-radius:14px}
.mega-intro strong{display:block;font-size:18px;line-height:1.55;margin-top:8px}
.mega-intro p{font-size:14px;color:var(--muted);margin:8px 0 14px}
.mega-links{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.mega-links>a{padding:10px 12px;border-radius:10px;display:flex;flex-direction:column;transition:background .2s}
.mega-links>a:hover{background:var(--cloud)}
.mega-links span{font-weight:700}
.mega-links small{font-size:13px;color:var(--muted)}
.header-cta{height:46px;padding:0 17px;background:var(--navy);color:#fff;display:flex;align-items:center;gap:14px;border-radius:9px;font-size:14px;white-space:nowrap;transition:background .2s,transform .2s}
.header-cta:hover{background:var(--blue);transform:translateY(-1px)}
.header-cta b{width:24px;height:24px;display:grid;place-items:center;border:1px solid rgba(255,255,255,.4);border-radius:50%;font-weight:500}
.menu-toggle{display:none}
.hero{position:relative;isolation:isolate;overflow:hidden;background:var(--navy);color:#fff;min-height:620px}
.hero-background{position:absolute;inset:0;z-index:-2;background:linear-gradient(90deg,rgba(7,20,38,.94) 0%,rgba(7,20,38,.89) 48%,rgba(7,20,38,.7) 100%),url('/assets/mine.jpg') center/cover no-repeat;opacity:.96}
.hero::after{content:"";position:absolute;inset:0;z-index:-1;background:radial-gradient(ellipse at 22% 48%,rgba(31,113,212,.24),transparent 45%),linear-gradient(180deg,transparent 65%,rgba(5,15,29,.45))}
.hero-grid{min-height:560px;display:grid;grid-template-columns:1.02fr .98fr;align-items:center;gap:34px;padding-block:65px 48px}
.hero-copy{max-width:590px;position:relative;z-index:2}
.hero-kicker{display:inline-flex;align-items:center;gap:10px;font-size:14px;color:#c8d8e8;letter-spacing:.01em}
.hero-kicker i,.photo-dot{width:8px;height:8px;border-radius:50%;background:var(--cyan);box-shadow:0 0 0 5px rgba(113,215,227,.12)}
.hero h1{font-size:clamp(42px,5vw,68px);line-height:1.25;letter-spacing:-.045em;margin:22px 0 18px;font-weight:850}
.hero h1 em{font-style:normal;color:#80d8e4}
.hero-copy>p{color:#d3dfeb;font-size:18px;max-width:540px;line-height:2;margin:0}
.hero-actions{display:flex;flex-wrap:wrap;gap:12px;margin-top:30px}
.button{min-height:50px;padding:10px 22px;display:inline-flex;align-items:center;justify-content:center;border:1px solid transparent;border-radius:9px;font-weight:700;font-size:15px;transition:background .2s,color .2s,border-color .2s,transform .2s;cursor:pointer}
.button:hover{transform:translateY(-2px)}
.button-primary{background:var(--blue);color:#fff;box-shadow:0 10px 22px rgba(25,113,212,.2)}
.button-primary:hover{background:#0e5ebd}
.button-outline-light{border-color:rgba(255,255,255,.5);color:#fff;background:rgba(255,255,255,.05)}
.button-outline-light:hover{background:rgba(255,255,255,.12);border-color:#fff}
.button-outline-dark{border-color:#b9c7d6;color:var(--navy);background:#fff}
.button-outline-dark:hover{border-color:var(--blue);color:var(--blue)}
.button-dark{background:var(--navy);color:#fff}
.button-dark:hover{background:#17365e}
.button-white{background:#fff;color:var(--navy)}
.button-white:hover{background:#e6f1ff}
.hero-proof{display:flex;align-items:center;gap:12px;margin-top:36px;color:#c4d1df;font-size:14px}
.hero-proof-icon{width:32px;height:32px;display:grid;place-items:center;border:1px solid rgba(255,255,255,.3);border-radius:50%;font-size:12px;color:var(--cyan)}
.hero-proof-icon svg{width:17px;height:17px}
.hero-visual{position:relative;min-height:440px;display:grid;place-items:center}
.hero-visual::before{content:"";position:absolute;width:min(440px,88%);aspect-ratio:1;border:1px solid rgba(137,203,232,.16);border-radius:50%;box-shadow:0 0 0 28px rgba(255,255,255,.018),0 0 90px rgba(61,151,220,.2) inset}
.hero-visual::after{content:"";position:absolute;width:60%;aspect-ratio:1;border-radius:50%;background:radial-gradient(circle,rgba(49,139,228,.28),transparent 68%);filter:blur(15px)}
.hero-visual img{width:min(475px,100%);max-height:450px;object-fit:contain;position:relative;z-index:1;filter:drop-shadow(0 26px 30px rgba(0,0,0,.34))}
.hero-orbit{position:absolute;border:1px dashed rgba(117,212,229,.22);border-radius:50%;z-index:0}
.orbit-one{width:92%;aspect-ratio:1;transform:rotate(-14deg)}
.orbit-two{width:78%;aspect-ratio:1;transform:rotate(31deg)}
.hero-photo-label{position:absolute;top:22px;right:7%;z-index:2;display:flex;align-items:center;gap:9px;color:#dbe7f2;font-size:13px;background:rgba(7,20,38,.68);border:1px solid rgba(255,255,255,.14);padding:8px 12px;border-radius:99px;backdrop-filter:blur(10px)}
.photo-dot{width:6px;height:6px}
.hero-product-note{position:absolute;bottom:42px;left:3%;z-index:3;background:#fff;color:var(--navy);padding:14px 19px;border-radius:12px;box-shadow:0 18px 45px rgba(0,0,0,.24);display:grid;min-width:175px;line-height:1.55}
.hero-product-note .note-label{font-size:12px;color:var(--muted)}
.hero-product-note strong{font-size:20px}
.hero-product-note small{font-size:13px;color:#516782}
.hero-plus{position:absolute;color:var(--cyan);font-size:27px;font-weight:300}
.plus-a{top:16%;left:15%}.plus-b{bottom:21%;right:12%}
.hero-bottom{height:60px;display:flex;align-items:center;gap:18px;color:#b5c6d8;font-size:13px;border-top:1px solid rgba(255,255,255,.14)}
.hero-line{height:1px;background:rgba(255,255,255,.23);width:min(150px,14vw)}
.process-strip{background:#fff;border-bottom:1px solid var(--line);box-shadow:0 12px 28px rgba(12,32,57,.04)}
.process-grid{min-height:132px;display:grid;grid-template-columns:1fr 45px 1fr 45px 1fr 45px 1fr;align-items:center}
.process-step{display:grid;grid-template-columns:52px 1fr;grid-template-rows:auto auto;column-gap:13px;align-items:center;padding:18px 12px;border-radius:14px;transition:background .2s}
.process-step:hover{background:var(--cloud)}
.process-symbol{grid-row:span 2;width:48px;height:48px;border-radius:14px;background:#e7f1fb;color:var(--blue);display:grid;place-items:center;font-size:13px;font-weight:800}
.process-step strong{font-size:16px}
.process-step small{color:var(--muted);font-size:13px;line-height:1.5}
.process-connector{height:1px;background:var(--line);position:relative}
.process-connector::after{content:"";position:absolute;left:0;top:-3px;width:7px;height:7px;border-left:1px solid #9cadbf;border-bottom:1px solid #9cadbf;transform:rotate(45deg)}
.section{padding-block:90px}
.section-light{background:var(--cloud)}
.section-heading{max-width:710px;margin:0 0 36px}
.section-heading h2{font-size:clamp(28px,3.4vw,42px);line-height:1.45;color:var(--navy);margin:9px 0 12px;font-weight:800;letter-spacing:-.025em}
.section-heading>p{font-size:16px;color:var(--muted);margin:0;max-width:650px}
.eyebrow{font-size:14px;color:var(--blue);font-weight:700;letter-spacing:.03em}
.eyebrow-light{color:#82dce7}
.text-gradient{background:linear-gradient(110deg,#1573d5,#63bed3);-webkit-background-clip:text;background-clip:text;color:transparent}
.product-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:20px}
.product-card{background:#fff;border:1px solid var(--line);border-radius:16px;overflow:hidden;display:flex;flex-direction:column;min-width:0;transition:transform .25s,box-shadow .25s,border-color .25s}
.product-card:hover{transform:translateY(-5px);box-shadow:0 18px 44px rgba(18,46,79,.11);border-color:#bdd4ec}
.product-card-image{position:relative;display:grid;place-items:center;background:#f6f8fb;height:218px;overflow:hidden}
.product-card-image img{width:100%;height:100%;object-fit:contain;padding:14px;transition:transform .35s}
.product-card:hover .product-card-image img{transform:scale(1.035)}
.product-card-category{position:absolute;top:12px;right:12px;padding:5px 10px;background:rgba(255,255,255,.92);border:1px solid rgba(213,224,236,.9);border-radius:99px;color:#334c67;font-size:12px;line-height:1.5}
.product-card-body{padding:18px 18px 17px;display:flex;flex-direction:column;flex:1}
.product-code{margin:0 0 5px;font-size:13px;color:var(--blue);font-weight:800;letter-spacing:.05em;direction:ltr;text-align:right}
.product-card h3{font-size:17px;line-height:1.65;margin:0 0 16px;font-weight:750;color:var(--navy)}
.product-card h3 a:hover{color:var(--blue)}
.text-link{font-weight:750;color:var(--blue);font-size:14px;display:inline-flex;align-items:center;gap:8px}
.text-link:hover{text-decoration:underline;text-underline-offset:4px}
.product-card .text-link{margin-top:auto}
.section-action{display:flex;justify-content:center;margin-top:34px}
.section-showcase{background:#0f2745;color:#fff;position:relative;overflow:hidden}
.section-showcase::before{content:"";position:absolute;width:480px;height:480px;border:1px solid rgba(127,216,228,.11);border-radius:50%;right:-160px;top:-170px;box-shadow:0 0 0 38px rgba(255,255,255,.018),0 0 0 85px rgba(255,255,255,.015)}
.showcase-grid{display:grid;grid-template-columns:1fr .95fr;gap:90px;align-items:center;position:relative}
.showcase-copy{max-width:540px}
.showcase-copy h2{font-size:clamp(30px,3.6vw,46px);line-height:1.45;margin:9px 0 14px}
.showcase-copy p{color:#c3d3e4;margin:0;max-width:520px}
.showcase-copy .button{margin-top:26px}
.showcase-steps{display:grid;gap:13px}
.showcase-step{display:grid;grid-template-columns:52px 1fr;gap:17px;align-items:start;padding:18px 20px;border:1px solid rgba(255,255,255,.14);border-radius:14px;background:rgba(255,255,255,.045)}
.showcase-step>span{width:38px;height:38px;border-radius:50%;border:1px solid rgba(113,215,227,.55);display:grid;place-items:center;color:var(--cyan);font-size:14px}
.showcase-step strong{font-size:17px}
.showcase-step p{margin:3px 0 0;color:#bdcde0;font-size:14px}
.article-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}
.article-card{background:#fff;border:1px solid var(--line);border-radius:16px;overflow:hidden;transition:transform .22s,box-shadow .22s}
.article-card:hover{transform:translateY(-4px);box-shadow:0 18px 42px rgba(19,44,73,.1)}
.article-visual{height:190px;position:relative;overflow:hidden;display:flex;align-items:flex-end;padding:18px;background:linear-gradient(125deg,#0b2543,#1b5d91)}
.article-visual::before,.article-page-image::before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 74% 28%,rgba(122,221,232,.42),transparent 30%),linear-gradient(145deg,transparent 35%,rgba(1,11,27,.62))}
.article-visual::after,.article-page-image::after{content:"";position:absolute;width:200px;height:200px;border-radius:50%;border:1px solid rgba(255,255,255,.25);right:55%;top:-30px;box-shadow:0 0 0 20px rgba(255,255,255,.03),0 0 0 48px rgba(255,255,255,.025)}
.article-choosing-a-mill{background:linear-gradient(130deg,#102341,#356791)}
.article-gravity-separation{background:linear-gradient(130deg,#102a44,#3b7685)}
.article-sample-preparation{background:linear-gradient(130deg,#112640,#314d6d)}
.article-visual-label{position:relative;z-index:2;color:#fff;font-size:13px;background:rgba(6,21,39,.42);border:1px solid rgba(255,255,255,.2);padding:6px 11px;border-radius:99px;backdrop-filter:blur(6px)}
.article-visual-mark{position:absolute;z-index:1;left:24px;top:16px;color:rgba(255,255,255,.18);font-size:36px;font-weight:900;letter-spacing:-.07em}
.article-card-body{padding:20px}
.article-category{font-size:13px;color:var(--blue);font-weight:750}
.article-card h3{font-size:19px;line-height:1.55;margin:8px 0}
.article-card p{font-size:14px;color:var(--muted);margin:0 0 15px}
.contact-band{padding-block:64px;background:#eaf3fb;border-top:1px solid #dbe8f4}
.contact-band-inner{display:flex;align-items:center;justify-content:space-between;gap:28px}
.contact-band h2{font-size:clamp(24px,3vw,34px);line-height:1.4;color:var(--navy);margin:7px 0}
.contact-band p{margin:0;color:var(--muted)}
.site-footer{background:#09192d;color:#d8e2ed;padding-top:55px}
.footer-grid{display:grid;grid-template-columns:1.3fr .7fr .9fr 1fr;gap:45px;padding-bottom:40px}
.footer-brand p{max-width:310px;color:#aebed0;font-size:14px;margin:17px 0 0}
.brand-light .brand-copy strong{color:#fff}
.brand-light .brand-copy small{color:#aebed0}
.brand-light .brand-mark{color:#7ed7e4}
.site-footer h2{font-size:15px;color:#fff;margin:0 0 15px}
.site-footer ul{list-style:none;padding:0;margin:0;display:grid;gap:7px}
.site-footer li,.footer-contact>a,.footer-contact>p{font-size:14px;color:#b7c5d5}
.site-footer a:hover{color:#7ed7e4}
.footer-contact{display:flex;flex-direction:column;align-items:flex-start;gap:5px}
.footer-contact p{margin:0 0 7px}
.footer-bottom{min-height:62px;border-top:1px solid rgba(255,255,255,.14);display:flex;align-items:center;justify-content:space-between;gap:20px;color:#9fb0c4;font-size:13px}
.floating-call{position:fixed;z-index:40;bottom:22px;left:22px;background:var(--blue);color:#fff;display:flex;align-items:center;gap:9px;border-radius:999px;padding:10px 16px;box-shadow:0 10px 28px rgba(18,91,175,.28);font-size:14px;font-weight:700;transition:transform .2s,background .2s}
.floating-call:hover{background:#0d5ebd;transform:translateY(-2px)}
.call-symbol{font-size:16px}
.breadcrumbs{display:flex;align-items:center;gap:11px;padding-block:18px;color:var(--muted);font-size:13px}
.breadcrumbs a:hover{color:var(--blue)}
.crumb-sep{width:6px;height:6px;border-bottom:1px solid #a2b0c0;border-inline-start:1px solid #a2b0c0;transform:rotate(45deg)}
.page-hero{background:linear-gradient(122deg,#0a1c34,#12385d);color:#fff;overflow:hidden;position:relative}
.page-hero::after{content:"";position:absolute;width:430px;height:430px;border-radius:50%;border:1px solid rgba(113,215,227,.12);right:-130px;top:-170px;box-shadow:0 0 0 30px rgba(255,255,255,.018),0 0 0 70px rgba(255,255,255,.014)}
.page-hero-grid{min-height:290px;padding-block:48px;display:flex;align-items:center;justify-content:space-between;gap:38px;position:relative;z-index:1}
.page-hero h1{font-size:clamp(35px,4.3vw,54px);line-height:1.35;margin:8px 0 12px;letter-spacing:-.03em}
.page-hero p{max-width:700px;color:#c8d9e9;margin:0;font-size:17px}
.page-hero-mark,.about-mark{width:190px;height:190px;border:1px solid rgba(128,216,230,.3);border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;flex:0 0 auto;position:relative;color:#8edce6}
.page-hero-mark::before,.about-mark::before{content:"";position:absolute;inset:12px;border:1px dashed rgba(128,216,230,.22);border-radius:50%}
.page-hero-mark span{font-size:42px;font-weight:800;line-height:1.2}
.page-hero-mark small,.about-mark small{font-size:13px;color:#c2d7e7}
.page-hero-about{background:linear-gradient(122deg,#0a1c34,#155273)}
.about-mark span{font-size:55px;font-weight:850}
.page-hero-contact{background:linear-gradient(122deg,#0a1c34,#185d76)}
.contact-hero-card{display:flex;flex-direction:column;gap:5px;padding:23px 26px;min-width:235px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.2);border-radius:16px;backdrop-filter:blur(10px)}
.contact-hero-card span,.contact-hero-card small{color:#c5d7e4;font-size:13px}
.contact-hero-card a{font-size:24px;font-weight:800;color:#fff;direction:ltr;text-align:right}
.page-hero-faq{background:linear-gradient(120deg,#0a1c34,#224b72)}
.page-hero-services{background:linear-gradient(120deg,#0a1c34,#194e69)}
.page-hero-articles{background:linear-gradient(120deg,#0a1c34,#235076)}
.page-hero-products{background:linear-gradient(120deg,#0a1c34,#17416b)}
.catalog-toolbar{display:flex;align-items:center;justify-content:space-between;gap:20px;margin-bottom:18px}
.search-box{display:flex;align-items:center;gap:12px;height:54px;max-width:490px;width:100%;border:1px solid var(--line);background:#fff;border-radius:10px;padding:0 16px}
.search-box:focus-within{border-color:#6fa8de;box-shadow:0 0 0 4px rgba(25,113,212,.08)}
.search-icon{width:17px;height:17px;border:1.7px solid #7890aa;border-radius:50%;position:relative;flex:0 0 auto}
.search-icon::after{content:"";width:7px;height:1.7px;background:#7890aa;position:absolute;bottom:-3px;left:-5px;transform:rotate(-45deg)}
.search-box input{border:0;outline:0!important;width:100%;min-width:0;background:transparent;color:var(--ink);font-size:15px}
.catalog-count{font-size:14px;color:var(--muted);margin:0}
.filter-chips{display:flex;flex-wrap:wrap;gap:9px;margin:0 0 28px}
.filter-chip{padding:8px 15px;border:1px solid var(--line);background:#fff;border-radius:99px;color:#42566d;font-size:14px;cursor:pointer;transition:all .2s}
.filter-chip:hover,.filter-chip.is-active{border-color:var(--blue);background:var(--blue);color:#fff}
.catalog-grid{grid-template-columns:repeat(4,minmax(0,1fr))}
.catalog-grid .product-card{min-height:365px}
.empty-state{padding:28px;border:1px dashed #b8c8da;border-radius:12px;text-align:center;color:var(--muted)}
.product-detail-hero{background:linear-gradient(120deg,#f3f7fb 0%,#eaf1f7 100%);overflow:hidden}
.product-detail-grid{display:grid;grid-template-columns:1.05fr .95fr;align-items:center;gap:45px;min-height:500px;padding-block:40px}
.product-detail-copy{padding-block:25px}
.product-detail-code{display:inline-block;margin:12px 0 4px;color:var(--blue);font-weight:850;font-size:14px;letter-spacing:.08em;direction:ltr}
.product-detail-copy h1{font-size:clamp(34px,4vw,49px);line-height:1.4;color:var(--navy);margin:0 0 12px;letter-spacing:-.03em}
.lead{font-size:18px;color:#53677e;line-height:1.9;margin:0}
.product-detail-actions{display:flex;flex-wrap:wrap;gap:10px;margin-top:25px}
.product-detail-mini{display:flex;flex-wrap:wrap;gap:13px;margin-top:24px;color:#687c91;font-size:13px}
.product-detail-mini span{padding-inline-start:13px;border-inline-start:1px solid #c6d2df}
.product-detail-visual{position:relative;min-height:420px;display:grid;place-items:center;margin:0}
.product-image-glow{position:absolute;width:360px;aspect-ratio:1;border-radius:50%;background:radial-gradient(circle,#d2e6f8,transparent 72%)}
.product-detail-visual img{width:min(470px,100%);max-height:440px;object-fit:contain;position:relative;filter:drop-shadow(0 22px 18px rgba(23,53,82,.13))}
.product-detail-visual figcaption{position:absolute;bottom:4px;right:50%;transform:translateX(50%);font-size:12px;color:#8999aa;white-space:nowrap}
.product-tabs{display:flex;gap:30px;overflow:auto;border-bottom:1px solid var(--line);padding-block:17px;font-size:14px;color:#4e627a}
.product-tabs a{white-space:nowrap}
.product-tabs a:hover{color:var(--blue)}
.product-overview{padding-top:72px}
.detail-copy-grid,.feature-section-grid,.specs-section-grid,.faq-section-grid{display:grid;grid-template-columns:.72fr 1.28fr;gap:60px;align-items:start}
.long-copy p{color:#53677e;margin:0 0 16px}
.feature-list{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:1fr 1fr;gap:12px}
.feature-list li{display:flex;align-items:flex-start;gap:12px;padding:16px 17px;border:1px solid var(--line);border-radius:12px;background:#fff;color:#334960}
.check-mark{width:20px;height:20px;display:inline-grid;place-items:center;flex:0 0 auto;margin-top:2px;border-radius:50%;background:#e3f2fb;color:var(--blue)}
.check-mark::after{content:"";width:7px;height:4px;border-bottom:1.5px solid currentColor;border-left:1.5px solid currentColor;transform:rotate(-45deg);margin-top:-2px}
.specs-section-grid{grid-template-columns:.7fr 1.3fr}
.spec-table-wrap{overflow:auto;border:1px solid var(--line);border-radius:14px;background:#fff}
.spec-table{width:100%;border-collapse:collapse;text-align:right;min-width:460px}
.spec-table tr:not(:last-child){border-bottom:1px solid #e7edf3}
.spec-table th,.spec-table td{padding:13px 17px;vertical-align:top}
.spec-table th{width:40%;font-weight:650;color:#51657c;background:#f7f9fc}
.spec-table td{color:#1b3049;font-weight:600}
.spec-note{font-size:13px;color:#78889a;margin:13px 0 0}
.faq-section-grid{grid-template-columns:.7fr 1.3fr}
.faq-list{display:grid;gap:10px}
.faq-item{border:1px solid var(--line);border-radius:12px;background:#fff;overflow:hidden}
.faq-item summary{cursor:pointer;list-style:none;padding:15px 18px;font-size:15px;font-weight:750;color:#1d334e;display:flex;align-items:center;justify-content:space-between;gap:14px}
.faq-item summary::-webkit-details-marker{display:none}
.faq-item summary::after{content:"";width:9px;height:9px;border-inline-start:1.7px solid var(--blue);border-bottom:1.7px solid var(--blue);transform:rotate(-45deg);flex:0 0 auto;transition:transform .2s}
.faq-item[open] summary::after{transform:rotate(135deg)}
.faq-answer{padding:0 18px 15px;color:#5b6f84}
.faq-answer p{margin:0;font-size:14px}
.about-intro-grid{display:grid;grid-template-columns:.72fr 1.28fr;gap:60px;align-items:start}
.about-image-section{background:#0f2745;color:#fff;padding-block:70px}
.about-image-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:60px;align-items:center}
.about-image{height:390px;border-radius:18px;overflow:hidden;position:relative}
.about-image img{width:100%;height:100%;object-fit:cover}
.image-caption{position:absolute;bottom:14px;right:14px;color:#fff;background:rgba(7,20,38,.7);padding:6px 12px;border-radius:8px;font-size:13px}
.about-image-copy h2{font-size:clamp(27px,3.2vw,40px);line-height:1.5;margin:8px 0 12px}
.about-image-copy p{color:#c4d4e5}
.about-image-copy .button{margin-top:14px}
.about-process-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.about-process-grid>div{padding:21px;border:1px solid var(--line);border-radius:14px;background:#fff}
.about-process-grid .process-symbol{margin-bottom:14px}
.about-process-grid h3{font-size:17px;margin:0 0 4px}
.about-process-grid p{font-size:14px;color:var(--muted);margin:0}
.service-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:19px}
.service-card{padding:26px;background:#fff;border:1px solid var(--line);border-radius:16px;position:relative;overflow:hidden}
.service-card::after{content:"";width:130px;height:130px;border:1px solid #e8eef5;border-radius:50%;position:absolute;left:-45px;top:-45px}
.service-index{position:absolute;left:22px;top:17px;font-size:12px;color:#9eafc2;letter-spacing:.06em}
.service-icon{display:grid;place-items:center;width:68px;height:68px;background:#e9f3fb;color:var(--blue);border-radius:16px;font-size:13px;font-weight:800}
.service-card h3{font-size:20px;color:var(--navy);margin:20px 0 8px}
.service-card p{font-size:15px;color:var(--muted);min-height:83px;margin:0 0 16px}
.section-dark{background:#0f2745;color:#fff}
.section-heading-light h2{color:#fff}
.section-heading-light>p{color:#bfd0e2}
.service-steps{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.service-steps>div{border-top:1px solid rgba(255,255,255,.22);padding:20px 10px 0}
.service-steps span{width:34px;height:34px;border:1px solid rgba(113,215,227,.6);border-radius:50%;color:var(--cyan);display:grid;place-items:center;font-size:14px}
.service-steps h3{margin:13px 0 2px;font-size:18px}
.service-steps p{color:#bdcde0;margin:0;font-size:14px}
.faq-page-grid{display:grid;grid-template-columns:.72fr 1.28fr;gap:60px;align-items:start}
.faq-page-grid .long-copy{margin-bottom:20px}
.contact-page-grid{display:grid;grid-template-columns:.8fr 1.2fr;gap:55px;align-items:start}
.contact-info h2,.contact-form-card h2{font-size:30px;line-height:1.45;margin:7px 0 8px;color:var(--navy)}
.contact-info>p,.contact-form-card>p{color:var(--muted);margin:0 0 24px}
.contact-method{display:flex;align-items:center;gap:14px;padding:14px 0;border-bottom:1px solid var(--line)}
.contact-method-icon{min-width:57px;height:48px;border-radius:10px;background:#e9f3fb;color:var(--blue);display:grid;place-items:center;font-size:12px;font-weight:800}
.contact-method>span:last-child{display:flex;flex-direction:column;line-height:1.55}
.contact-method strong{font-size:16px;direction:ltr;text-align:right}
.contact-method small{font-size:13px;color:var(--muted)}
.address-card{margin-top:18px;padding:18px;background:var(--cloud);border-radius:12px}
.address-label{color:var(--blue);font-size:13px;font-weight:800}
.address-card p{margin:4px 0 8px;color:#344960}
.contact-form-card{background:#f6f9fc;border:1px solid var(--line);border-radius:18px;padding:28px}
.contact-form-card form{display:grid;gap:14px}
.contact-form-card label{display:grid;gap:6px;font-size:14px;font-weight:700;color:#314760}
.contact-form-card label span{font-weight:400;color:#7b8b9c}
.contact-form-card input,.contact-form-card select,.contact-form-card textarea{width:100%;border:1px solid #d3dee9;background:#fff;border-radius:8px;padding:11px 12px;color:var(--ink);font-size:15px}
.contact-form-card input::placeholder,.contact-form-card textarea::placeholder{color:#9aa8b6}
.contact-form-card textarea{resize:vertical}
.form-row{display:grid;grid-template-columns:1fr 1fr;gap:13px}
.form-submit{width:max-content;min-width:220px}
.form-note{font-size:13px;color:#6c7c8d;margin:-3px 0 0}
.article-page{padding-bottom:30px}
.article-page-header{max-width:850px;margin:20px auto 28px;padding-inline:24px}
.article-page-header h1{font-size:clamp(34px,4.5vw,54px);line-height:1.4;color:var(--navy);margin:8px 0}
.article-page-header .lead{font-size:18px}
.article-meta{display:flex;gap:10px;margin-top:16px;color:#718195;font-size:13px}
.article-meta span+span{border-inline-start:1px solid #c7d2de;padding-inline-start:10px}
.article-page-image{height:330px;max-width:var(--max);width:calc(100% - 48px);margin:0 auto 45px;border-radius:18px;position:relative;overflow:hidden;background:linear-gradient(130deg,#102341,#356791);display:flex;align-items:flex-end;padding:24px}
.article-page-image.article-choosing-a-mill{background:linear-gradient(130deg,#102341,#356791)}
.article-page-image.article-gravity-separation{background:linear-gradient(130deg,#102a44,#3b7685)}
.article-page-image.article-sample-preparation{background:linear-gradient(130deg,#112640,#314d6d)}
.article-body{max-width:760px;margin:0 auto;padding-inline:24px}
.article-body section{margin:0 0 30px}
.article-body h2{font-size:24px;color:var(--navy);margin:0 0 8px}
.article-body p{color:#53677e;margin:0 0 12px}
.article-callout{margin-top:38px;padding:24px;background:#edf5fb;border-radius:15px;border:1px solid #d8e7f4}
.article-callout strong{font-size:18px;color:var(--navy)}
.article-callout p{margin:6px 0 16px}
.article-callout .button{min-height:44px}
.not-found{min-height:480px;display:grid;align-items:center;background:linear-gradient(120deg,#f2f6fa,#e8f0f7)}
.not-found h1{font-size:clamp(34px,5vw,54px);color:var(--navy);margin:7px 0}
.not-found p{color:var(--muted)}
.visually-hidden{position:absolute!important;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
body.has-motion [data-reveal]{opacity:0;transform:translateY(12px);transition:opacity .55s ease,transform .55s ease}
body.has-motion [data-reveal].is-visible{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*::before,*::after{transition-duration:.01ms!important;animation-duration:.01ms!important;animation-iteration-count:1!important}body.has-motion [data-reveal]{opacity:1;transform:none}}
@media (max-width:1050px){.primary-nav{gap:16px;font-size:14px}.header-inner{gap:20px}.brand-copy strong{font-size:16px}.header-cta{padding-inline:12px}.product-grid,.catalog-grid{grid-template-columns:repeat(3,minmax(0,1fr))}.showcase-grid{gap:45px}.footer-grid{gap:28px}.product-detail-grid{gap:20px}}
@media (max-width:820px){.container{width:min(100% - 36px,var(--max))}.utility-inner{height:34px}.utility-inner>span{display:none}.utility-inner{justify-content:center}.site-header{height:76px}.header-inner{gap:14px}.menu-toggle{display:flex;flex-direction:column;justify-content:center;gap:5px;width:42px;height:42px;border:1px solid var(--line);border-radius:9px;background:#fff;cursor:pointer;order:3}.menu-toggle span{width:18px;height:1.5px;background:var(--navy);margin-inline:auto;transition:transform .2s,opacity .2s}.menu-toggle[aria-expanded=true] span:first-child{transform:translateY(6.5px) rotate(45deg)}.menu-toggle[aria-expanded=true] span:nth-child(2){opacity:0}.menu-toggle[aria-expanded=true] span:last-child{transform:translateY(-6.5px) rotate(-45deg)}.brand{margin-inline-start:auto}.brand-mark{width:38px;height:38px}.brand-copy strong{font-size:15px}.brand-copy small{font-size:11px}.header-cta{height:42px;font-size:13px;gap:7px}.header-cta b{display:none}.primary-nav{position:absolute;top:100%;right:0;left:0;height:auto;max-height:calc(100vh - 120px);overflow:auto;background:#fff;display:none;flex-direction:column;align-items:stretch;gap:0;padding:8px 18px 16px;border-bottom:1px solid var(--line);box-shadow:0 16px 30px rgba(13,36,65,.11);margin:0}.primary-nav.is-open{display:flex}.primary-nav>a,.nav-products>summary{height:auto;min-height:48px;border-bottom:1px solid #edf1f5}.primary-nav>a::after,.nav-products>summary::after{display:none}.nav-products{height:auto}.nav-products>summary{justify-content:space-between}.mega-menu{position:static;width:auto;padding:12px 0 5px;border:0;box-shadow:none;border-radius:0;grid-template-columns:1fr;gap:10px}.mega-intro{display:none}.mega-links{grid-template-columns:1fr 1fr}.mega-links>a{padding:10px;background:#f7f9fc}.hero{min-height:auto}.hero-grid{min-height:unset;padding-block:58px 30px;grid-template-columns:1fr 1fr;gap:10px}.hero h1{font-size:clamp(38px,7vw,58px)}.hero-copy>p{font-size:16px}.hero-visual{min-height:350px}.hero-visual img{max-height:350px}.hero-bottom{height:52px}.process-grid{grid-template-columns:1fr 25px 1fr;gap:5px 0;padding-block:10px}.process-step:nth-of-type(n+5){display:none}.process-connector:nth-of-type(4){display:none}.process-step{padding:12px 6px;grid-template-columns:42px 1fr;column-gap:9px}.process-symbol{width:40px;height:40px;border-radius:12px}.section{padding-block:70px}.product-grid,.catalog-grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}.product-card-image{height:190px}.product-card-body{padding:15px}.product-card h3{font-size:16px}.showcase-grid{grid-template-columns:1fr;gap:35px}.showcase-copy{max-width:700px}.article-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.article-card:last-child:nth-child(odd){grid-column:span 2}.footer-grid{grid-template-columns:1fr 1fr}.page-hero-grid{min-height:250px}.page-hero-mark,.about-mark{width:150px;height:150px}.product-detail-grid{grid-template-columns:1fr 1fr;min-height:420px}.product-detail-visual{min-height:330px}.product-detail-visual img{max-height:330px}.detail-copy-grid,.feature-section-grid,.specs-section-grid,.faq-section-grid,.about-intro-grid,.faq-page-grid{grid-template-columns:1fr;gap:24px}.about-image-grid{gap:35px}.contact-page-grid{grid-template-columns:1fr;gap:35px}}
@media (max-width:560px){body{font-size:16px}.container{width:calc(100% - 30px)}.utility-links{gap:13px;font-size:13px}.site-header{height:70px}.brand-mark{width:34px;height:34px}.brand-copy strong{font-size:14px}.brand-copy small{display:none}.header-inner{gap:9px}.header-cta{height:39px;padding-inline:10px;font-size:12px}.menu-toggle{width:38px;height:38px}.hero-grid{grid-template-columns:1fr;gap:10px;padding-block:48px 22px}.hero-copy{max-width:none}.hero h1{font-size:42px;margin:15px 0 11px}.hero-copy>p{font-size:15px}.hero-actions{margin-top:22px}.button{min-height:46px;padding-inline:16px;font-size:14px}.hero-proof{margin-top:20px}.hero-visual{min-height:310px;margin-top:0}.hero-visual img{max-height:315px;width:90%}.hero-visual::before{width:78%}.hero-product-note{bottom:22px;left:0;padding:10px 13px;min-width:150px}.hero-product-note strong{font-size:18px}.hero-photo-label{top:8px;right:2%;font-size:11px;padding:6px 9px}.hero-bottom{font-size:11px;gap:10px}.hero-line{width:34px}.process-grid{grid-template-columns:1fr 16px 1fr;padding-block:8px}.process-step{grid-template-columns:36px 1fr;column-gap:7px;padding:10px 1px}.process-symbol{width:34px;height:34px;font-size:11px}.process-step strong{font-size:14px}.process-step small{font-size:11px}.process-connector{width:14px}.section{padding-block:58px}.section-heading{margin-bottom:25px}.section-heading h2{font-size:28px}.section-heading>p{font-size:15px}.product-grid,.catalog-grid{grid-template-columns:1fr 1fr;gap:10px}.product-card-image{height:150px}.product-card-image img{padding:7px}.product-card-category{top:7px;right:7px;font-size:10px;padding:3px 7px}.product-card-body{padding:12px 11px 13px}.product-code{font-size:11px}.product-card h3{font-size:14px;line-height:1.55;margin-bottom:10px}.text-link{font-size:12px;gap:5px}.section-action{margin-top:25px}.showcase-step{grid-template-columns:42px 1fr;padding:14px}.showcase-step>span{width:34px;height:34px}.article-grid{grid-template-columns:1fr;gap:14px}.article-card:last-child:nth-child(odd){grid-column:auto}.article-visual{height:165px}.article-card-body{padding:17px}.article-card h3{font-size:17px}.contact-band{padding-block:45px}.contact-band-inner{align-items:flex-start;flex-direction:column}.contact-band h2{font-size:25px}.site-footer{padding-top:40px}.footer-grid{grid-template-columns:1fr 1fr;gap:28px 18px}.footer-brand{grid-column:span 2}.footer-brand p{max-width:450px}.site-footer h2{font-size:14px}.site-footer li,.footer-contact>a,.footer-contact>p{font-size:13px}.footer-contact{grid-column:span 2}.footer-bottom{align-items:flex-start;flex-direction:column;justify-content:center;padding-block:13px;gap:2px;font-size:12px}.floating-call{bottom:13px;left:13px;padding:9px 13px;font-size:13px}.breadcrumbs{font-size:12px;padding-block:14px;gap:7px}.page-hero-grid{min-height:auto;padding-block:38px;gap:14px}.page-hero h1{font-size:34px}.page-hero p{font-size:15px}.page-hero-mark,.about-mark{width:105px;height:105px}.page-hero-mark::before,.about-mark::before{inset:7px}.page-hero-mark span{font-size:28px}.page-hero-mark small,.about-mark small{font-size:10px;text-align:center}.about-mark span{font-size:37px}.catalog-toolbar{align-items:stretch;flex-direction:column;gap:8px}.search-box{max-width:none;height:48px}.catalog-count{font-size:13px}.filter-chips{gap:7px;margin-bottom:20px}.filter-chip{font-size:12px;padding:6px 10px}.catalog-grid .product-card{min-height:300px}.product-detail-grid{grid-template-columns:1fr;gap:0;padding-block:26px 22px}.product-detail-copy{padding-block:5px}.product-detail-copy h1{font-size:32px}.product-detail-copy .lead{font-size:16px}.product-detail-visual{min-height:260px;grid-row:1}.product-detail-visual img{max-height:270px;width:90%}.product-detail-visual figcaption{bottom:0;font-size:10px}.product-image-glow{width:240px}.product-detail-actions{margin-top:18px}.product-detail-mini{gap:7px;margin-top:17px;font-size:11px}.product-detail-mini span{padding-inline-start:8px}.product-tabs{gap:20px;padding-block:13px;font-size:13px}.product-overview{padding-top:52px}.feature-list{grid-template-columns:1fr;gap:8px}.feature-list li{padding:13px;font-size:14px}.spec-table{min-width:410px}.spec-table th,.spec-table td{padding:11px 12px;font-size:14px}.about-image-section{padding-block:48px}.about-image-grid{grid-template-columns:1fr;gap:26px}.about-image{height:250px}.about-image-copy h2{font-size:27px}.about-process-grid{grid-template-columns:1fr 1fr;gap:9px}.about-process-grid>div{padding:14px}.about-process-grid h3{font-size:15px}.about-process-grid p{font-size:12px}.service-grid{grid-template-columns:1fr;gap:12px}.service-card{padding:20px}.service-card p{min-height:unset}.service-steps{grid-template-columns:1fr;gap:20px}.service-steps>div{display:grid;grid-template-columns:40px 1fr;column-gap:12px}.service-steps span{grid-row:span 2}.service-steps h3{margin:0}.service-steps p{grid-column:2}.faq-page-grid,.contact-page-grid{gap:25px}.contact-info h2,.contact-form-card h2{font-size:25px}.contact-form-card{padding:19px}.form-row{grid-template-columns:1fr;gap:14px}.form-submit{width:100%}.article-page-header{margin:15px auto 22px;padding-inline:15px}.article-page-header h1{font-size:32px}.article-page-header .lead{font-size:16px}.article-page-image{width:calc(100% - 30px);height:220px;margin-bottom:30px}.article-body{padding-inline:18px}.article-body h2{font-size:21px}.article-body p{font-size:15px}.not-found{min-height:390px}}

/* Chireh mobile redesign: touch-first layouts for every page */
@media (max-width: 820px) {
  html { scroll-padding-top: 82px; }
  body { overflow-x: hidden; }
  .container { width: calc(100% - 36px); }

  .utility-bar { font-size: 13px; }
  .utility-inner { height: 34px; justify-content: center; }
  .utility-inner > span { display: none; }
  .utility-links { gap: 12px; white-space: nowrap; }
  .utility-separator { display: none; }

  .site-header { height: 72px; z-index: 70; }
  .header-inner {
    display: grid;
    grid-template-columns: 42px minmax(0, 1fr) auto;
    align-items: center;
    gap: 8px;
    position: relative;
  }
  .menu-toggle {
    grid-column: 1;
    grid-row: 1;
    order: 0;
    width: 42px;
    height: 42px;
    border-radius: 13px;
    background: #f4f8fc;
    border-color: #dce5ef;
  }
  .brand {
    grid-column: 2;
    grid-row: 1;
    justify-self: start;
    min-width: 0;
    margin: 0;
    gap: 8px;
  }
  .brand-mark { width: 38px; height: 38px; }
  .brand-copy { min-width: 0; }
  .brand-copy strong { font-size: 14px; white-space: nowrap; }
  .brand-copy small { display: block; font-size: 11px; }
  .header-cta {
    grid-column: 3;
    grid-row: 1;
    justify-self: end;
    height: 42px;
    min-height: 42px;
    padding-inline: 12px;
    border-radius: 999px;
    white-space: nowrap;
    font-size: 14px;
  }
  .header-cta b { display: none; }
  .primary-nav {
    display: none;
    position: absolute;
    top: calc(100% + 8px);
    right: 0;
    left: 0;
    width: auto;
    max-height: calc(100dvh - 92px);
    overflow-x: hidden;
    overflow-y: auto;
    overscroll-behavior: contain;
    padding: 10px;
    margin: 0;
    gap: 4px;
    border: 1px solid #dce5ef;
    border-radius: 20px;
    background: rgba(255, 255, 255, .98);
    box-shadow: 0 22px 55px rgba(10, 30, 55, .2);
    backdrop-filter: blur(18px);
  }
  .primary-nav.is-open { display: flex; }
  .primary-nav > a,
  .nav-products > summary {
    display: flex;
    align-items: center;
    min-height: 50px;
    height: auto;
    padding: 0 14px;
    border: 0;
    border-radius: 12px;
    font-size: 15px;
  }
  .primary-nav > a[aria-current="page"],
  .nav-products > summary[aria-current="page"],
  .nav-products[open] > summary {
    color: var(--blue);
    background: #edf6ff;
  }
  .primary-nav > a::after,
  .nav-products > summary::after { display: none; }
  .nav-products { height: auto; }
  .mega-menu {
    position: static;
    width: auto;
    margin: 5px 0 7px;
    padding: 10px;
    grid-template-columns: 1fr;
    gap: 9px;
    border: 1px solid var(--line);
    border-radius: 15px;
    background: #f8fbfe;
    box-shadow: none;
  }
  .mega-intro {
    display: block;
    padding: 13px;
    border: 1px solid #e1ebf4;
    border-radius: 12px;
    background: linear-gradient(135deg, #edf6ff, #f9fcff);
  }
  .mega-intro strong { font-size: 15px; }
  .mega-intro p { margin: 5px 0 0; font-size: 14px; }
  .mega-intro .text-link { display: none; }
  .mega-links { grid-template-columns: 1fr; gap: 5px; }
  .mega-links > a {
    display: flex;
    align-items: center;
    justify-content: space-between;
    min-height: 48px;
    padding: 9px 12px;
    border: 1px solid #e7eef5;
    border-radius: 11px;
    background: #fff;
  }
  .mega-links > a span { font-size: 14px; }
  .mega-links > a small { font-size: 12px; }

  .hero { min-height: 0; border-radius: 0 0 24px 24px; }
  .hero-grid {
    min-height: 0;
    padding-block: 38px 20px;
    grid-template-columns: 1fr;
    gap: 16px;
  }
  .hero-copy { max-width: none; }
  .hero-kicker { max-width: 100%; font-size: 13px; line-height: 1.7; }
  .hero h1 { font-size: clamp(36px, 9vw, 46px); line-height: 1.3; margin: 13px 0 10px; }
  .hero-copy > p { max-width: 40ch; font-size: 16px; line-height: 1.85; }
  .hero-actions { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 9px; }
  .hero-actions .button { width: 100%; padding-inline: 10px; text-align: center; }
  .hero-proof { margin-top: 18px; }
  .hero-visual {
    min-height: 315px;
    margin: 0;
    border: 1px solid rgba(255,255,255,.16);
    border-radius: 21px;
    background: linear-gradient(145deg, rgba(255,255,255,.1), rgba(255,255,255,.025));
  }
  .hero-visual img { width: 88%; max-height: 295px; object-fit: contain; }
  .hero-photo-label { top: 10px; right: 10px; max-width: 78%; font-size: 13px; }
  .hero-product-note { bottom: 14px; left: 12px; }
  .hero-bottom { height: auto; padding-block: 14px; gap: 10px; font-size: 13px; }

  .process-grid {
    min-height: 0;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 9px;
    padding-block: 14px;
  }
  .process-connector { display: none; }
  .process-step {
    min-width: 0;
    min-height: 84px;
    grid-template-columns: 42px minmax(0, 1fr);
    padding: 11px;
    gap: 0 9px;
    border: 1px solid var(--line);
    border-radius: 15px;
    background: #fff;
  }
  .process-symbol { width: 40px; height: 40px; border-radius: 12px; }
  .process-step strong { font-size: 14px; }
  .process-step small { font-size: 13px; line-height: 1.5; }

  .section { padding-block: 54px; }
  .section-heading { margin-bottom: 23px; }
  .section-heading h2 { font-size: clamp(25px, 6vw, 31px); line-height: 1.55; }
  .section-heading > p { font-size: 15px; line-height: 1.85; }
  .section-action { margin-top: 24px; }
  .contact-band { padding-block: 42px; }
  .contact-band-inner { align-items: stretch; flex-direction: column; gap: 16px; }
  .contact-band .button { width: 100%; }

  .product-grid,
  .catalog-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; }
  .product-card { min-width: 0; border-radius: 15px; }
  .product-card:hover { transform: none; box-shadow: none; }
  .product-card-image { height: 158px; }
  .product-card-image img { padding: 10px; }
  .product-card-body { display: flex; flex: 1; flex-direction: column; align-items: flex-start; padding: 13px; }
  .product-card h3 { font-size: 14px; line-height: 1.65; }
  .product-card-body .text-link { min-height: 42px; margin-top: auto; }
  .product-card-category { font-size: 12px; }
  .filter-chips {
    display: flex;
    overflow-x: auto;
    overscroll-behavior-inline: contain;
    gap: 8px;
    padding: 2px 1px 7px;
    margin-bottom: 14px;
    scrollbar-width: none;
  }
  .filter-chips::-webkit-scrollbar,
  .product-tabs::-webkit-scrollbar,
  .breadcrumbs::-webkit-scrollbar { display: none; }
  .filter-chip { flex: 0 0 auto; min-height: 42px; padding: 7px 13px; font-size: 14px; }
  .catalog-toolbar { align-items: stretch; flex-direction: column; gap: 10px; }
  .search-box { width: 100%; max-width: none; min-height: 50px; }

  .page-hero::after { width: 270px; height: 270px; right: -105px; top: -110px; }
  .page-hero-grid {
    min-height: 0;
    display: grid;
    grid-template-columns: minmax(0, 1fr) 88px;
    align-items: center;
    gap: 12px;
    padding-block: 30px;
  }
  .page-hero h1 { font-size: clamp(27px, 6.8vw, 34px); line-height: 1.45; }
  .page-hero p { max-width: 42ch; font-size: 15px; line-height: 1.8; }
  .page-hero-mark { width: 86px; height: 86px; }
  .page-hero-mark span { font-size: 22px; }
  .page-hero-mark small { font-size: 12px; }
  .breadcrumbs {
    width: calc(100% - 36px);
    overflow-x: auto;
    gap: 8px;
    padding-block: 13px;
    white-space: nowrap;
    scrollbar-width: none;
  }

  .product-detail-grid {
    min-height: 0;
    grid-template-columns: 1fr;
    gap: 7px;
    padding-block: 22px 25px;
  }
  .product-detail-visual {
    grid-row: 1;
    min-height: 280px;
    border-radius: 20px;
  }
  .product-detail-visual img { width: 88%; max-height: 260px; object-fit: contain; }
  .product-detail-copy { padding-block: 13px 0; }
  .product-detail-copy h1 { font-size: clamp(27px, 7vw, 34px); line-height: 1.5; }
  .product-detail-copy .lead { font-size: 16px; line-height: 1.85; }
  .product-detail-actions { display: grid; grid-template-columns: 1fr; gap: 9px; }
  .product-detail-actions .button { width: 100%; }
  .product-detail-mini { display: flex; flex-wrap: wrap; gap: 8px; }
  .product-tabs {
    position: sticky;
    top: 72px;
    z-index: 30;
    display: flex;
    overflow-x: auto;
    gap: 20px;
    padding-block: 12px;
    white-space: nowrap;
    background: rgba(255,255,255,.97);
    scrollbar-width: none;
  }
  .product-tabs a { flex: 0 0 auto; min-height: 32px; }
  .product-overview { padding-top: 44px; }
  .detail-copy-grid,
  .feature-section-grid,
  .specs-section-grid,
  .faq-section-grid,
  .about-intro-grid,
  .faq-page-grid,
  .contact-page-grid {
    grid-template-columns: 1fr;
    gap: 20px;
  }
  .feature-list { grid-template-columns: 1fr; gap: 8px; }
  .feature-list li { padding: 14px; font-size: 15px; }
  .spec-table-wrap { overflow: hidden; border-radius: 14px; }
  .spec-table { width: 100%; min-width: 0; table-layout: fixed; }
  .spec-table th { width: 42%; }
  .spec-table td { width: 58%; }
  .spec-table th,
  .spec-table td {
    padding: 11px 10px;
    overflow-wrap: anywhere;
    font-size: 14px;
    line-height: 1.65;
  }
  .spec-note { font-size: 13px; line-height: 1.7; }

  .showcase-grid { grid-template-columns: 1fr; gap: 20px; }
  .showcase-copy { padding: 22px; border-radius: 20px; }
  .showcase-copy h2 { font-size: 27px; line-height: 1.5; }
  .showcase-steps { display: grid; gap: 9px; }
  .showcase-step { grid-template-columns: 42px minmax(0, 1fr); padding: 14px; border: 1px solid rgba(255,255,255,.12); border-radius: 15px; }
  .article-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; }
  .article-card { border-radius: 15px; }
  .article-card:hover { transform: none; box-shadow: none; }
  .article-visual { height: 165px; padding: 13px; }
  .article-card-body { padding: 14px; }
  .article-card h3 { font-size: 15px; line-height: 1.65; }
  .article-page-header { margin: 14px auto 22px; padding-inline: 18px; }
  .article-page-header h1 { font-size: clamp(28px, 7vw, 36px); line-height: 1.5; }
  .article-page-header .lead { font-size: 16px; }
  .article-meta { flex-wrap: wrap; row-gap: 6px; font-size: 13px; }
  .article-page-image { width: calc(100% - 36px); height: 250px; margin-bottom: 28px; border-radius: 16px; }
  .article-body { padding-inline: 18px; }
  .article-body h2 { font-size: 22px; line-height: 1.55; }
  .article-body p { font-size: 16px; line-height: 1.9; }
  .article-callout { margin-top: 24px; padding: 18px; border-radius: 16px; }
  .article-callout .button { width: 100%; }

  .about-image-section { padding-block: 52px; }
  .about-image-grid { grid-template-columns: 1fr; gap: 20px; }
  .about-image { height: 260px; border-radius: 17px; }
  .about-image-copy h2 { font-size: 27px; line-height: 1.55; }
  .about-process-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 9px; }
  .about-process-grid > div { padding: 14px; border-radius: 14px; }
  .about-process-grid h3 { font-size: 15px; line-height: 1.55; }
  .about-process-grid p { font-size: 14px; line-height: 1.7; }
  .service-grid { grid-template-columns: 1fr; gap: 12px; }
  .service-card { padding: 21px; border-radius: 17px; }
  .service-icon { width: 56px; height: 56px; border-radius: 15px; }
  .service-steps { grid-template-columns: 1fr; gap: 10px; }
  .service-steps > div { display: grid; grid-template-columns: 42px minmax(0, 1fr); column-gap: 11px; align-items: start; }
  .service-steps span { grid-row: span 2; }

  .faq-page-grid { gap: 18px; }
  .faq-item { border-radius: 15px; }
  .faq-item > summary { min-height: 58px; padding: 13px 15px; font-size: 15px; line-height: 1.7; }
  .faq-answer { padding: 0 15px 15px; }
  .faq-answer p { font-size: 15px; line-height: 1.85; }

  .contact-page-grid { gap: 20px; }
  .contact-info h2,
  .contact-form-card h2 { font-size: 26px; line-height: 1.5; }
  .contact-method { min-height: 68px; gap: 11px; padding-block: 12px; }
  .contact-method-icon { min-width: 48px; height: 46px; }
  .contact-method strong { overflow-wrap: anywhere; font-size: 14px; }
  .contact-method small { font-size: 13px; }
  .contact-form-card { padding: 20px; border-radius: 18px; }
  .form-row { grid-template-columns: 1fr; gap: 13px; }
  .contact-form-card input,
  .contact-form-card select,
  .contact-form-card textarea {
    width: 100%;
    min-height: 50px;
    border-radius: 12px;
    font-size: 16px;
  }
  .contact-form-card textarea { min-height: 135px; }
  .form-submit { width: 100%; min-height: 50px; }
  .form-note { font-size: 13px; line-height: 1.7; }

  .privacy-body { width: calc(100% - 36px); max-width: 760px; margin-inline: auto; }
  .privacy-body p { font-size: 16px; line-height: 1.9; }
  .not-found { min-height: 350px; padding-block: 36px; }
  .not-found h1 { font-size: 34px; line-height: 1.45; }

  .site-footer { padding-top: 42px; }
  .footer-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 22px 16px;
    padding-bottom: 28px;
  }
  .footer-brand,
  .footer-contact { grid-column: 1 / -1; }
  .footer-brand p { max-width: 50ch; font-size: 14px; }
  .site-footer h2 { margin-bottom: 10px; font-size: 15px; }
  .site-footer li a,
  .footer-contact > a { display: flex; align-items: center; min-height: 42px; overflow-wrap: anywhere; }
  .footer-contact { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 4px 12px; }
  .footer-contact > h2,
  .footer-contact > p { grid-column: 1 / -1; }
  .footer-bottom { align-items: flex-start; flex-direction: column; gap: 8px; padding-block: 16px; }
  .floating-call {
    bottom: calc(14px + env(safe-area-inset-bottom));
    left: 14px;
    min-height: 48px;
    padding: 10px 15px;
    font-size: 14px;
  }
}

@media (max-width: 560px) {
  .container { width: calc(100% - 30px); }
  .header-inner { grid-template-columns: 38px minmax(0, 1fr) auto; gap: 6px; }
  .menu-toggle { width: 38px; height: 38px; }
  .brand-mark { width: 34px; height: 34px; }
  .brand-copy strong { font-size: 14px; }
  .brand-copy small { display: none; }
  .header-cta { min-height: 40px; height: 40px; padding-inline: 10px; font-size: 14px; }
  .primary-nav { max-height: calc(100dvh - 86px); }
  .utility-links { gap: 11px; font-size: 12.5px; }

  .hero-grid { padding-block: 32px 18px; }
  .hero h1 { font-size: clamp(34px, 9.4vw, 41px); }
  .hero-actions { grid-template-columns: 1fr; }
  .hero-visual { min-height: 275px; }
  .hero-visual img { max-height: 258px; }
  .hero-bottom { font-size: 12px; }

  .section { padding-block: 48px; }
  .section-heading { margin-bottom: 20px; }
  .section-heading h2 { font-size: 27px; }
  .product-grid,
  .catalog-grid { gap: 10px; }
  .product-card-image { height: 140px; }
  .product-card-body { padding: 11px; }
  .product-card h3 { font-size: 14px; }
  .product-card-body .text-link { font-size: 14px; }
  .catalog-toolbar { gap: 8px; }
  .filter-chips { gap: 7px; }
  .page-hero-grid { grid-template-columns: minmax(0, 1fr) 76px; gap: 9px; padding-block: 25px; }
  .page-hero-mark { width: 74px; height: 74px; }
  .page-hero-mark span { font-size: 20px; }
  .page-hero-mark small { font-size: 11px; }
  .page-hero h1 { font-size: clamp(26px, 7vw, 31px); }
  .page-hero p { font-size: 14px; }

  .product-detail-visual { min-height: 245px; }
  .product-detail-visual img { max-height: 225px; }
  .product-detail-copy h1 { font-size: 29px; }
  .product-tabs { top: 68px; gap: 18px; }
  .spec-table th,
  .spec-table td { padding: 10px 8px; font-size: 13.5px; }
  .spec-table th { width: 44%; }
  .spec-table td { width: 56%; }

  .article-grid { grid-template-columns: 1fr; gap: 14px; }
  .article-visual { height: 170px; }
  .article-card-body { padding: 16px; }
  .article-page-header { padding-inline: 15px; }
  .article-page-image { width: calc(100% - 30px); height: 215px; margin-bottom: 23px; }
  .article-body { padding-inline: 16px; }
  .article-body h2 { font-size: 21px; }

  .about-image { height: 235px; }
  .about-process-grid { grid-template-columns: 1fr 1fr; }
  .service-card { padding: 18px; }
  .contact-form-card { padding: 17px; }
  .contact-info h2,
  .contact-form-card h2 { font-size: 24px; }

  .footer-grid { column-gap: 12px; row-gap: 20px; }
  .footer-contact { column-gap: 9px; }
  .footer-contact > a { font-size: 14px; }
  .footer-bottom { font-size: 13px; }
  .floating-call { left: 12px; bottom: calc(12px + env(safe-area-inset-bottom)); }
}

@media (max-width: 380px) {
  .container { width: calc(100% - 24px); }
  .header-inner { grid-template-columns: 36px minmax(0, 1fr) auto; gap: 5px; }
  .menu-toggle { width: 36px; height: 36px; }
  .brand { gap: 6px; }
  .brand-mark { width: 32px; height: 32px; }
  .brand-copy strong { font-size: 13px; }
  .header-cta { padding-inline: 8px; font-size: 13px; }
  .product-card-image { height: 126px; }
  .product-card-body { padding: 10px; }
  .product-card h3 { font-size: 14px; }
  .page-hero-grid { grid-template-columns: minmax(0, 1fr) 66px; }
  .page-hero-mark { width: 64px; height: 64px; }
  .spec-table th,
  .spec-table td { padding: 9px 7px; }
  .footer-grid { column-gap: 10px; }
}

/* Product mega menu: spacious desktop panel and touch-first mobile layout */
.header-inner { position: relative; }
.nav-products { position: static; }
.nav-products > summary { gap: 8px; }
.nav-products > summary::after {
  content: "";
  width: auto;
  height: 2px;
  margin: 0;
  border: 0;
  position: absolute;
  right: 0;
  left: 100%;
  bottom: 20px;
  background: var(--blue);
  transform: none;
  transition: left .25s ease;
}
.nav-products > summary:hover::after,
.nav-products[open] > summary::after { left: 0; }
.nav-chevron {
  width: 7px;
  height: 7px;
  border-inline-start: 1.5px solid currentColor;
  border-bottom: 1.5px solid currentColor;
  transform: rotate(-45deg);
  margin-top: -4px;
  transition: transform .2s ease, margin .2s ease;
}
.nav-products[open] > summary .nav-chevron { transform: rotate(135deg); margin-top: 4px; }
.mega-menu {
  position: absolute;
  z-index: 100;
  top: calc(100% + 9px);
  right: 0;
  left: 0;
  width: min(1160px, calc(100vw - 48px));
  margin-inline: auto;
  padding: 15px;
  display: grid;
  grid-template-columns: minmax(210px, .82fr) minmax(420px, 1.55fr) minmax(210px, .82fr);
  gap: 12px;
  border: 1px solid #dce7f2;
  border-radius: 24px;
  background: #fff;
  box-shadow: 0 28px 78px rgba(8, 27, 52, .2);
  animation: mega-menu-in .2s ease both;
}
@keyframes mega-menu-in {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}
.mega-intro {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  min-height: 100%;
  padding: 21px;
  border-radius: 19px;
  color: #fff;
  background:
    radial-gradient(circle at 8% 92%, rgba(94, 203, 220, .2), transparent 38%),
    linear-gradient(145deg, #0b1c34 0%, #133b63 100%);
}
.mega-intro::before {
  content: "";
  position: absolute;
  z-index: -1;
  left: -54px;
  bottom: -82px;
  width: 188px;
  height: 188px;
  border: 1px solid rgba(151, 220, 231, .24);
  border-radius: 50%;
  box-shadow: 0 0 0 18px rgba(151, 220, 231, .035), 0 0 0 37px rgba(151, 220, 231, .03);
}
.mega-kicker { display: inline-flex; align-items: center; gap: 8px; color: #a7dce4; font-size: 12px; font-weight: 700; }
.mega-kicker i { width: 7px; height: 7px; border-radius: 50%; background: var(--cyan); box-shadow: 0 0 0 5px rgba(113, 215, 227, .12); }
.mega-intro h2 { max-width: 300px; margin: 15px 0 8px; color: #fff; font-size: 20px; line-height: 1.65; font-weight: 800; }
.mega-intro p { margin: 0; color: #c7d7e7; font-size: 13px; line-height: 1.9; }
.mega-process { display: flex; align-items: center; gap: 5px; flex-wrap: wrap; margin-top: 17px; color: #9fb8d0; font-size: 10px; }
.mega-process span { padding: 5px 8px; border: 1px solid rgba(210, 229, 243, .17); border-radius: 999px; color: #e6f1f9; background: rgba(255, 255, 255, .055); }
.mega-process b { font-size: 11px; font-weight: 500; color: var(--cyan); }
.mega-all-link { display: flex; align-items: center; justify-content: space-between; gap: 12px; margin-top: 19px; padding: 10px 12px; border-radius: 11px; color: #fff; background: #1971d4; font-size: 12px; font-weight: 700; transition: background .2s, transform .2s; }
.mega-all-link:hover { color: #fff; background: #2f8ae9; transform: translateY(-1px); }
.mega-all-link b { font-size: 17px; font-weight: 500; line-height: 1; }
.mega-categories { min-width: 0; padding: 15px; border: 1px solid #e7edf4; border-radius: 19px; background: #f8fafd; }
.mega-heading { display: flex; align-items: end; justify-content: space-between; gap: 10px; margin: 0 1px 12px; }
.mega-overline { color: #718197; font-size: 11px; font-weight: 700; }
.mega-heading h3 { margin: 3px 0 0; color: var(--navy); font-size: 17px; line-height: 1.5; }
.mega-count { flex: 0 0 auto; padding: 5px 9px; border: 1px solid #e2eaf3; border-radius: 999px; color: #60758c; background: #fff; font-size: 10px; }
.mega-links { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 7px; }
.mega-category { min-width: 0; min-height: 66px; display: grid; grid-template-columns: 38px minmax(0, 1fr) 12px; align-items: center; gap: 9px; padding: 8px 9px; border: 1px solid transparent; border-radius: 14px; color: var(--ink); background: #fff; transition: border-color .2s, box-shadow .2s, transform .2s; }
.mega-category:hover { border-color: #d5e5f5; color: var(--ink); box-shadow: 0 8px 20px rgba(19, 51, 83, .07); transform: translateY(-1px); }
.mega-icon { width: 38px; height: 38px; display: grid; place-items: center; border-radius: 12px; color: #1971d4; background: #eaf3ff; }
.mega-category:nth-child(2) .mega-icon { color: #bc6a25; background: #fff1e5; }
.mega-category:nth-child(3) .mega-icon { color: #167f83; background: #e5f7f5; }
.mega-category:nth-child(4) .mega-icon { color: #7356bf; background: #f0ecff; }
.mega-category:nth-child(5) .mega-icon { color: #14729a; background: #e7f5fb; }
.mega-icon svg { width: 21px; height: 21px; stroke: currentColor; stroke-width: 1.6; stroke-linecap: round; stroke-linejoin: round; }
.mega-copy { min-width: 0; display: flex; flex-direction: column; gap: 2px; }
.mega-copy strong { overflow: hidden; color: #17324e; font-size: 12px; line-height: 1.55; text-overflow: ellipsis; white-space: nowrap; }
.mega-copy small { overflow: hidden; color: #75869a; font-size: 10px; line-height: 1.5; text-overflow: ellipsis; white-space: nowrap; }
.mega-arrow { color: #9aabbd; font-size: 14px; font-weight: 400; transition: color .2s, transform .2s; }
.mega-category:hover .mega-arrow { color: var(--blue); transform: translateX(-2px); }
.mega-category:last-child { grid-column: 1 / -1; }
.mega-feature { position: relative; min-width: 0; min-height: 100%; display: flex; flex-direction: column; justify-content: space-between; overflow: hidden; padding: 14px; border: 1px solid #dcecf2; border-radius: 19px; color: var(--ink); background: linear-gradient(155deg, #f3f8ff 0%, #edf8f8 100%); transition: border-color .2s, box-shadow .2s, transform .2s; }
.mega-feature::before { content: ""; position: absolute; width: 180px; height: 180px; top: 42px; right: 50%; transform: translateX(50%); border-radius: 50%; background: radial-gradient(circle, rgba(114, 189, 222, .2), rgba(114, 189, 222, 0) 68%); pointer-events: none; }
.mega-feature:hover { border-color: #b7d8e8; color: var(--ink); box-shadow: 0 10px 26px rgba(19, 51, 83, .09); transform: translateY(-1px); }
.mega-feature-tag { align-self: flex-start; z-index: 1; padding: 5px 9px; border: 1px solid #dbe8f2; border-radius: 999px; color: #54718c; background: rgba(255,255,255,.8); font-size: 10px; font-weight: 700; }
.mega-feature-art { position: relative; z-index: 1; min-height: 132px; display: grid; place-items: center; }
.mega-feature-art img { width: 100%; height: 132px; object-fit: contain; filter: drop-shadow(0 12px 9px rgba(20, 48, 73, .12)); }
.mega-feature-badge { position: absolute; left: 0; bottom: 5px; padding: 5px 8px; border: 1px solid #dbe8f2; border-radius: 999px; color: #34516e; background: rgba(255,255,255,.92); font-size: 10px; }
.mega-feature-copy { position: relative; z-index: 1; display: flex; flex-direction: column; align-items: flex-start; }
.mega-feature-copy small { color: #718197; font-size: 10px; }
.mega-feature-copy strong { margin-top: 1px; color: #102945; font-size: 22px; letter-spacing: .02em; }
.mega-feature-copy em { display: flex; align-items: center; gap: 5px; margin-top: 5px; color: var(--blue); font-size: 11px; font-style: normal; font-weight: 700; }
.mega-feature-copy em b { font-size: 14px; font-weight: 500; }
@media (min-width: 821px) and (max-width: 1050px) {
  .mega-menu { grid-template-columns: minmax(0, 1.2fr) minmax(0, 1fr); width: min(940px, calc(100vw - 36px)); }
  .mega-feature { grid-column: 1 / -1; min-height: 105px; display: grid; grid-template-columns: 140px minmax(0, 1fr); align-items: center; }
  .mega-feature-art { grid-column: 1; grid-row: 1 / span 2; min-height: 70px; }
  .mega-feature-art img { height: 78px; }
  .mega-feature-copy { grid-column: 2; grid-row: 1 / span 2; }
  .mega-feature-tag { position: absolute; top: 10px; left: 10px; }
}
@media (max-width: 820px) {
  .header-inner { position: relative; }
  .nav-products { position: static; }
  .nav-products > summary { justify-content: space-between; }
  .primary-nav > a::after,
  .nav-products > summary::after { display: none; }
  .mega-menu { position: static; width: auto; margin: 3px 0 7px; padding: 10px; grid-template-columns: 1fr; gap: 9px; border: 1px solid #dce7f2; border-radius: 18px; box-shadow: none; animation: none; }
  .mega-intro { min-height: 0; padding: 14px; border-radius: 15px; }
  .mega-intro h2 { max-width: none; margin: 8px 0 5px; font-size: 17px; line-height: 1.55; }
  .mega-intro p { font-size: 12px; }
  .mega-process { display: none; }
  .mega-all-link { margin-top: 11px; padding: 8px 10px; }
  .mega-categories { padding: 10px; border: 0; background: transparent; }
  .mega-heading { margin: 0 1px 8px; }
  .mega-heading h3 { font-size: 14px; }
  .mega-overline { font-size: 10px; }
  .mega-count { padding: 4px 7px; font-size: 9px; }
  .mega-links { gap: 6px; }
  .mega-category { min-height: 67px; grid-template-columns: 32px minmax(0, 1fr) 10px; gap: 6px; padding: 7px; border-color: #edf1f6; border-radius: 12px; }
  .mega-icon { width: 32px; height: 32px; border-radius: 10px; }
  .mega-icon svg { width: 18px; height: 18px; }
  .mega-copy strong { font-size: 11px; white-space: normal; }
  .mega-copy small { font-size: 9px; white-space: normal; }
  .mega-feature { min-height: 94px; display: grid; grid-template-columns: 82px minmax(0,1fr); align-items: center; gap: 8px; padding: 10px; border-radius: 15px; }
  .mega-feature-art { grid-column: 1; grid-row: 1; min-height: 70px; }
  .mega-feature-art img { height: 70px; }
  .mega-feature-badge { left: 0; bottom: -4px; padding: 3px 5px; font-size: 8px; }
  .mega-feature-copy { grid-column: 2; grid-row: 1; }
  .mega-feature-copy small { font-size: 9px; }
  .mega-feature-copy strong { font-size: 18px; }
  .mega-feature-copy em { margin-top: 2px; font-size: 10px; }
  .mega-feature-tag { position: absolute; top: 7px; left: 8px; padding: 3px 6px; font-size: 8px; }
}
@media (max-width: 380px) {
  .mega-links { grid-template-columns: 1fr; }
  .mega-category:last-child { grid-column: auto; }
}

/* Chireh footer: industrial brand system for wide and touch layouts */
.footer-cta {
  position: relative;
  overflow: hidden;
  padding: 44px 0 0;
  color: #fff;
  background: #07172a;
}
.footer-cta-inner {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 34px;
  padding: 28px 34px;
  border: 1px solid rgba(152, 207, 228, .22);
  border-radius: 24px;
  background:
    radial-gradient(circle at 8% 115%, rgba(92, 198, 220, .19), transparent 34%),
    linear-gradient(115deg, #123d65 0%, #102b49 52%, #0d223d 100%);
  box-shadow: 0 22px 55px rgba(0, 0, 0, .18);
}
.footer-cta-inner::before {
  content: "";
  position: absolute;
  z-index: -1;
  left: -64px;
  top: -112px;
  width: 285px;
  height: 285px;
  border: 1px solid rgba(148, 215, 230, .16);
  border-radius: 50%;
  box-shadow: 0 0 0 20px rgba(148, 215, 230, .035), 0 0 0 42px rgba(148, 215, 230, .025);
}
.footer-cta-copy { position: relative; z-index: 1; max-width: 690px; }
.footer-cta-kicker { display: inline-flex; align-items: center; gap: 9px; color: #9de0e7; font-size: 12px; font-weight: 750; }
.footer-cta-kicker i { width: 7px; height: 7px; border-radius: 50%; background: var(--cyan); box-shadow: 0 0 0 5px rgba(113, 215, 227, .12); }
.footer-cta h2 { margin: 10px 0 6px; color: #fff; font-size: clamp(21px, 2.4vw, 28px); line-height: 1.55; }
.footer-cta p { margin: 0; color: #c3d3e3; font-size: 14px; line-height: 1.8; }
.footer-cta-actions { position: relative; z-index: 1; flex: 0 0 auto; display: flex; align-items: center; gap: 17px; }
.footer-cta-button { min-height: 49px; display: inline-flex; align-items: center; justify-content: space-between; gap: 18px; padding: 0 16px; border: 1px solid #3690ec; border-radius: 12px; color: #fff; background: #1971d4; box-shadow: 0 10px 25px rgba(11, 88, 169, .25); font-size: 14px; font-weight: 750; transition: transform .2s, background .2s, box-shadow .2s; white-space: nowrap; }
.footer-cta-button:hover { color: #fff; background: #2f8ae9; box-shadow: 0 12px 27px rgba(11, 88, 169, .35); transform: translateY(-2px); }
.footer-cta-button b { font-size: 18px; font-weight: 500; }
.footer-cta-phone { display: flex; flex-direction: column; gap: 2px; color: #e8f2fa; white-space: nowrap; }
.footer-cta-phone:hover { color: #9de0e7; }
.footer-cta-phone small { color: #a9bed2; font-size: 10px; }
.footer-cta-phone strong { font-size: 14px; letter-spacing: .02em; }

.site-footer {
  position: relative;
  overflow: hidden;
  padding: 36px 0 calc(72px + env(safe-area-inset-bottom));
  color: #d8e2ed;
  background:
    radial-gradient(ellipse at 92% 12%, rgba(25, 113, 212, .11), transparent 32%),
    #07172a;
}
.site-footer::before { content: ""; position: absolute; top: 0; right: max(24px, calc((100% - var(--max)) / 2)); left: max(24px, calc((100% - var(--max)) / 2)); height: 1px; background: linear-gradient(90deg, transparent, rgba(113, 215, 227, .38), transparent); }
.footer-grid { position: relative; display: grid; grid-template-columns: minmax(0, 1.25fr) minmax(125px, .75fr) minmax(180px, .95fr) minmax(250px, 1.15fr); gap: 34px; padding: 12px 0 34px; }
.footer-brand .brand { gap: 12px; }
.footer-brand p { max-width: 330px; margin: 18px 0 14px; color: #aebed0; font-size: 13px; line-height: 1.9; }
.brand-light .brand-copy strong { color: #fff; }
.brand-light .brand-copy small { color: #aebed0; }
.brand-light .brand-mark { color: #7ed7e4; }
.footer-brand-note { display: inline-flex; align-items: center; gap: 8px; padding: 7px 10px; border: 1px solid rgba(255, 255, 255, .1); border-radius: 999px; color: #b9d8e6; background: rgba(255, 255, 255, .035); font-size: 10px; }
.footer-brand-note i { width: 6px; height: 6px; border-radius: 50%; background: #71d7e3; box-shadow: 0 0 0 4px rgba(113, 215, 227, .1); }
.footer-column h2, .footer-contact h2 { display: flex; align-items: center; gap: 9px; margin: 0 0 15px; color: #fff; font-size: 14px; font-weight: 750; }
.footer-column h2::before, .footer-contact h2::before { content: ""; width: 3px; height: 17px; border-radius: 4px; background: linear-gradient(#71d7e3, #1971d4); }
.footer-column ul { display: grid; gap: 9px; list-style: none; margin: 0; padding: 0; }
.footer-column li { margin: 0; }
.footer-column li a { display: inline-flex; align-items: center; gap: 8px; color: #b7c5d5; font-size: 12px; line-height: 1.65; transition: color .18s, transform .18s; }
.footer-column li a::before { content: ""; width: 5px; height: 5px; border: 1px solid rgba(113, 215, 227, .55); border-radius: 1px; transform: rotate(45deg); transition: background .18s, border-color .18s; }
.footer-column li a:hover { color: #8fe0e8; transform: translateX(-2px); }
.footer-column li a:hover::before { border-color: #71d7e3; background: #71d7e3; }
.footer-contact { display: block; min-width: 0; }
.footer-address { display: grid; grid-template-columns: 33px minmax(0, 1fr); align-items: start; gap: 9px; margin: 0 0 12px; color: #b7c5d5; font-size: 11px; line-height: 1.8; }
.footer-contact-icon { width: 33px; height: 33px; display: grid; place-items: center; flex: 0 0 auto; border: 1px solid rgba(146, 192, 217, .18); border-radius: 10px; color: #83d7e3; background: rgba(255, 255, 255, .045); }
.footer-contact-icon svg { width: 17px; height: 17px; stroke: currentColor; stroke-width: 1.6; stroke-linecap: round; stroke-linejoin: round; }
.footer-contact-cards { display: grid; grid-template-columns: 1fr 1fr; gap: 7px; }
.footer-contact-card { min-width: 0; min-height: 50px; display: grid; grid-template-columns: 31px minmax(0, 1fr); align-items: center; gap: 8px; padding: 7px; border: 1px solid rgba(255, 255, 255, .085); border-radius: 12px; color: #d8e2ed; background: rgba(255, 255, 255, .035); transition: border-color .18s, background .18s, transform .18s; }
.footer-contact-card:hover { border-color: rgba(113, 215, 227, .4); color: #fff; background: rgba(255, 255, 255, .07); transform: translateY(-1px); }
.footer-contact-card .footer-contact-icon { width: 31px; height: 31px; border-radius: 9px; }
.footer-contact-card .footer-contact-icon svg { width: 16px; height: 16px; }
.footer-contact-card > span:last-child { display: flex; min-width: 0; flex-direction: column; gap: 1px; }
.footer-contact-card small { color: #8ea4bb; font-size: 9px; line-height: 1.45; }
.footer-contact-card strong { overflow-wrap: anywhere; color: #d9e7f3; font-size: 10px; line-height: 1.5; font-weight: 650; direction: ltr; text-align: right; }
.footer-bottom { position: relative; min-height: 62px; display: flex; align-items: center; justify-content: space-between; gap: 20px; border-top: 1px solid rgba(255, 255, 255, .11); color: #8fa3b9; font-size: 11px; }
.footer-bottom-links { display: flex; align-items: center; gap: 18px; }
.footer-bottom-links a { display: inline-flex; align-items: center; gap: 5px; color: #aebed0; transition: color .18s; }
.footer-bottom-links a:hover { color: #8fe0e8; }
@media (max-width: 1100px) {
  .footer-grid { grid-template-columns: minmax(0, 1fr) minmax(0, .85fr); gap: 30px 42px; }
  .footer-contact-cards { max-width: 430px; }
}
@media (max-width: 820px) {
  .footer-cta { padding-top: 28px; }
  .footer-cta-inner { display: grid; grid-template-columns: 1fr; gap: 18px; padding: 22px; border-radius: 21px; }
  .footer-cta h2 { max-width: 35ch; margin-top: 9px; font-size: clamp(19px, 5vw, 24px); }
  .footer-cta p { font-size: 12px; line-height: 1.8; }
  .footer-cta-actions { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, .8fr); gap: 10px; }
  .footer-cta-button { min-height: 46px; padding-inline: 12px; font-size: 12px; }
  .footer-cta-phone { min-height: 46px; justify-content: center; padding-inline: 10px; border: 1px solid rgba(255, 255, 255, .13); border-radius: 12px; background: rgba(255, 255, 255, .04); }
  .footer-cta-phone strong { font-size: 12px; }
  .site-footer { padding-top: 25px; padding-bottom: calc(76px + env(safe-area-inset-bottom)); }
  .footer-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 25px 18px; padding-top: 10px; padding-bottom: 27px; }
  .footer-brand, .footer-contact { grid-column: 1 / -1; }
  .footer-brand p { max-width: 56ch; font-size: 13px; }
  .footer-column h2, .footer-contact h2 { margin-bottom: 11px; font-size: 13px; }
  .footer-column ul { gap: 5px; }
  .footer-column li a { min-height: 38px; font-size: 12px; }
  .footer-contact-cards { max-width: none; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 7px; }
  .footer-contact-card { min-height: 52px; padding: 7px 8px; }
  .footer-contact-card strong { font-size: 10px; }
  .footer-bottom { align-items: flex-start; flex-direction: column; gap: 10px; padding-block: 16px; font-size: 11px; }
  .footer-bottom-links { flex-wrap: wrap; gap: 14px; }
}
@media (max-width: 560px) {
  .footer-cta { padding-top: 22px; }
  .footer-cta-inner { padding: 19px; gap: 15px; }
  .footer-cta h2 { font-size: clamp(19px, 5.6vw, 23px); }
  .footer-cta-actions { grid-template-columns: 1fr 1fr; gap: 8px; }
  .footer-cta-button { min-height: 44px; gap: 8px; padding-inline: 10px; font-size: 11px; }
  .footer-cta-phone { padding-inline: 8px; }
  .footer-cta-phone small { font-size: 9px; }
  .footer-cta-phone strong { font-size: 11px; }
  .footer-grid { gap: 23px 14px; }
  .footer-brand p { margin: 14px 0 12px; font-size: 12px; }
  .footer-brand .brand-copy small { display: block; }
  .footer-contact-cards { gap: 6px; }
  .footer-contact-card { grid-template-columns: 28px minmax(0, 1fr); gap: 6px; padding: 6px; }
  .footer-contact-card .footer-contact-icon { width: 28px; height: 28px; }
  .footer-contact-card strong { font-size: 9px; }
  .footer-address { grid-template-columns: 30px minmax(0, 1fr); gap: 8px; font-size: 11px; }
  .footer-contact-icon { width: 30px; height: 30px; }
  .footer-bottom { font-size: 10px; }
}
@media (max-width: 380px) {
  .footer-cta-actions { grid-template-columns: 1fr; }
  .footer-contact-cards { grid-template-columns: 1fr; }
}
"""
(ASSETS / "site.css").write_text(CSS, encoding="utf-8")

JS = r"""
document.documentElement.classList.add("js-ready");
document.body.classList.add("has-motion");

(function(){
  var toggle=document.querySelector(".menu-toggle");
  var nav=document.querySelector(".primary-nav");
  if(toggle&&nav){
    toggle.addEventListener("click",function(){
      var open=toggle.getAttribute("aria-expanded")==="true";
      toggle.setAttribute("aria-expanded",String(!open));
      nav.classList.toggle("is-open",!open);
      toggle.setAttribute("aria-label",open?"بازکردن فهرست":"بستن فهرست");
    });
    var products=nav.querySelector(".nav-products");
    var productSummary=products&&products.querySelector("summary");
    var hoverCloseTimer;
    var openedByHover=false;
    function setProductsOpen(open){
      if(!products||!productSummary){return;}
      products.open=!!open;
      productSummary.setAttribute("aria-expanded",String(!!open));
      if(!open){openedByHover=false;}
    }
    if(products&&productSummary){
      products.addEventListener("toggle",function(){
        productSummary.setAttribute("aria-expanded",String(products.open));
      });
      products.addEventListener("pointerenter",function(){
        if(window.matchMedia("(min-width: 821px) and (hover: hover)").matches){
          window.clearTimeout(hoverCloseTimer);
          openedByHover=true;
          setProductsOpen(true);
        }
      });
      products.addEventListener("pointerleave",function(){
        if(window.matchMedia("(min-width: 821px) and (hover: hover)").matches){
          hoverCloseTimer=window.setTimeout(function(){
            if(!products.matches(":hover")&&!products.contains(document.activeElement)){setProductsOpen(false);}
          },180);
        }
      });
      products.addEventListener("focusout",function(event){
        if(window.matchMedia("(min-width: 821px)").matches&&!products.contains(event.relatedTarget)){
          hoverCloseTimer=window.setTimeout(function(){
            if(!products.matches(":hover")&&!products.contains(document.activeElement)){setProductsOpen(false);}
          },180);
        }
      });
      productSummary.addEventListener("click",function(event){
        if(openedByHover&&window.matchMedia("(min-width: 821px) and (hover: hover)").matches){
          event.preventDefault();
        }
      });
      productSummary.addEventListener("keydown",function(event){
        if(event.key==="ArrowDown"){
          event.preventDefault();
          setProductsOpen(true);
          var firstProductLink=products.querySelector(".mega-links a");
          if(firstProductLink){firstProductLink.focus();}
        }
      });
    }
    document.addEventListener("pointerdown",function(event){
      if(!nav.contains(event.target)&&!toggle.contains(event.target)){
        if(products){setProductsOpen(false);}
        if(nav.classList.contains("is-open")){
          nav.classList.remove("is-open");
          toggle.setAttribute("aria-expanded","false");
          toggle.setAttribute("aria-label","بازکردن فهرست");
        }
      }
    });
    nav.querySelectorAll("a").forEach(function(link){
      link.addEventListener("click",function(){
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded","false");
        toggle.setAttribute("aria-label","بازکردن فهرست");
        if(products){setProductsOpen(false);}
      });
    });
    document.addEventListener("keydown",function(event){
      if(event.key==="Escape"){
        var wasMobile=window.matchMedia("(max-width: 820px)").matches;
        var menuWasOpen=nav.classList.contains("is-open");
        var productsWereOpen=products&&products.open;
        if(products){setProductsOpen(false);}
        if(menuWasOpen){
          nav.classList.remove("is-open");
          toggle.setAttribute("aria-expanded","false");
          toggle.setAttribute("aria-label","بازکردن فهرست");
        }
        if(wasMobile&&menuWasOpen){toggle.focus();}
        else if(productsWereOpen&&productSummary){productSummary.focus();}
      }
    });
  }

  var path=window.location.pathname;
  var navSection=path.indexOf("/products")===0?"products":
    path.indexOf("/services")===0?"services":
    path.indexOf("/articles")===0?"articles":
    path.indexOf("/about")===0?"about":
    path.indexOf("/contact")===0?"contact":
    path.indexOf("/faq")===0?"faq":"home";
  var activeLink=document.querySelector('[data-nav="'+navSection+'"]');
  if(activeLink&&activeLink.tagName==="A"){activeLink.setAttribute("aria-current","page");}
  if(navSection==="products"){
    var productSummary=document.querySelector(".nav-products>summary");
    if(productSummary){productSummary.setAttribute("aria-current","page");}
  }

  var search=document.getElementById("product-search");
  var cards=Array.prototype.slice.call(document.querySelectorAll("[data-product-card]"));
  var chips=Array.prototype.slice.call(document.querySelectorAll("[data-filter]"));
  var count=document.getElementById("catalog-count");
  var empty=document.getElementById("empty-products");
  var activeCategory="all";
  var params=new URLSearchParams(window.location.search);
  if(search&&cards.length){
    var initialQuery=params.get("q")||"";
    var initialCategory=params.get("category")||"all";
    search.value=initialQuery;
    if(chips.some(function(chip){return chip.dataset.filter===initialCategory;})){activeCategory=initialCategory;}
    function filterCards(){
      var query=search.value.trim().toLocaleLowerCase("fa-IR");
      var visible=0;
      cards.forEach(function(card){
        var matchesText=card.textContent.toLocaleLowerCase("fa-IR").indexOf(query)!==-1;
        var matchesCategory=activeCategory==="all"||card.dataset.category===activeCategory;
        var show=matchesText&&matchesCategory;
        card.hidden=!show;
        if(show){visible+=1;}
      });
      if(count){count.textContent=visible.toLocaleString("fa-IR")+" تجهیز نمایش داده می‌شود";}
      if(empty){empty.hidden=visible!==0;}
      chips.forEach(function(chip){
        var active=chip.dataset.filter===activeCategory;
        chip.classList.toggle("is-active",active);
        chip.setAttribute("aria-pressed",String(active));
      });
    }
    chips.forEach(function(chip){
      chip.addEventListener("click",function(){
        activeCategory=chip.dataset.filter;
        filterCards();
      });
    });
    search.addEventListener("input",filterCards);
    filterCards();
  }

  var productInput=document.getElementById("contact-product");
  var productParam=params.get("product");
  if(productInput&&productParam){productInput.value=productParam;}
  var subjectParam=params.get("subject");
  var subjectSelect=document.getElementById("contact-subject");
  if(subjectSelect&&subjectParam){
    Array.prototype.slice.call(subjectSelect.options).forEach(function(option){
      if(option.textContent.indexOf(subjectParam)!==-1){subjectSelect.value=option.value;}
    });
  }

  var form=document.getElementById("contact-form");
  if(form){
    form.addEventListener("submit",function(event){
      event.preventDefault();
      if(!form.reportValidity()){return;}
      var data=new FormData(form);
      var subject=String(data.get("subject")||"درخواست از وب‌سایت");
      var body=[
        "نام: "+String(data.get("name")||""),
        "شماره تماس: "+String(data.get("phone")||""),
        "ایمیل: "+String(data.get("email")||""),
        "محصول: "+String(data.get("product")||""),
        "",
        "پیام:",
        String(data.get("message")||"")
      ].join("\n");
      var link="mailto:sales@chirehfg.com?subject="+encodeURIComponent(subject)+"&body="+encodeURIComponent(body);
      var status=document.getElementById("form-status");
      if(status){status.textContent="پیام آماده شد. برای ارسال، نرم‌افزار ایمیل خود را تأیید کنید.";}
      window.location.href=link;
    });
  }

  var year=document.getElementById("current-year");
  if(year){year.textContent=new Date().getFullYear().toLocaleString("fa-IR");}

  if("IntersectionObserver" in window&&!window.matchMedia("(prefers-reduced-motion: reduce)").matches){
    var observer=new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if(entry.isIntersecting){entry.target.classList.add("is-visible");observer.unobserve(entry.target);}
      });
    },{threshold:.12});
    document.querySelectorAll(".section-heading,.product-card,.article-card,.service-card,.showcase-step,[data-reveal]").forEach(function(el){
      el.setAttribute("data-reveal","");
      observer.observe(el);
    });
  }else{
    document.querySelectorAll("[data-reveal]").forEach(function(el){el.classList.add("is-visible");});
  }
})();
"""
(ASSETS / "site.js").write_text(JS, encoding="utf-8")

# Keep catalog source in the project root, not in the public static directory.
public_catalog = DIST / "products-source.json"
if public_catalog.exists():
    public_catalog.unlink()

# Robots file for the static publication. A sitemap is intentionally omitted until a public domain is assigned.
(DIST / "robots.txt").write_text("User-agent: *\nAllow: /\n", encoding="utf-8")
print("Built", len(products), "product cards and", len(DETAILS), "product pages.")
