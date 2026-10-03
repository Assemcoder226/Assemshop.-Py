import os
import webbrowser
import time
from http.server import SimpleHTTPRequestHandler, HTTPServer

# كود واجهة معرض الأعمال المتكامل والمحسن
html_content = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>معرض أعمال المطور</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        body { background-color: #f8fafc; color: #334155; padding: 25px 15px; line-height: 1.6; }
        .portfolio-container { max-width: 800px; margin: 0 auto; background: #ffffff; border-radius: 12px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05); padding: 25px; }
        .portfolio-header { text-align: center; margin-bottom: 25px; border-bottom: 2px dashed #e2e8f0; padding-bottom: 15px; }
        .portfolio-header h1 { font-size: 1.7rem; color: #1e293b; margin-bottom: 8px; }
        .portfolio-header p { font-size: 0.95rem; color: #64748b; }
        .visitor-form-section { background: #fef3c7; border: 1px solid #f59e0b; border-radius: 8px; padding: 18px; margin-bottom: 35px; }
        .form-title { font-size: 1rem; color: #b45309; margin-bottom: 12px; font-weight: bold; }
        .form-group input, .form-group textarea { width: 100%; padding: 11px; border: 1px solid #cbd5e1; border-radius: 6px; margin-bottom: 12px; outline: none; font-size: 0.9rem; }
        .btn-submit { width: 100%; background-color: #2563eb; color: white; border: none; padding: 12px; border-radius: 6px; font-weight: bold; cursor: pointer; font-size: 1rem; transition: 0.2s; }
        .btn-submit:hover { background-color: #1d4ed8; }
        .projects-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px; }
        .project-card { background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px; display: flex; flex-direction: column; justify-content: space-between; transition: all 0.3s ease; }
        .project-card:hover { border-color: #3b82f6; transform: translateY(-3px); box-shadow: 0 5px 15px rgba(0,0,0,0.05); }
        .project-icon-title { display: flex; align-items: center; gap: 8px; margin-bottom: 10px; }
        .project-icon { font-size: 1.3rem; }
        .project-title { font-size: 1.05rem; color: #1e293b; font-weight: bold; }
        .project-desc { font-size: 0.85rem; color: #64748b; margin-bottom: 15px; flex-grow: 1; }
        .project-link { font-size: 0.85rem; color: #2563eb; text-decoration: none; font-weight: bold; }
        .project-link:hover { text-decoration: underline; }
        .portfolio-footer { text-align: center; margin-top: 40px; font-size: 0.8rem; color: #94a3b8; border-top: 1px solid #e2e8f0; padding-top: 15px; }
    </style>
</head>
<body>
    <div class="portfolio-container">
        <header class="portfolio-header">
            <h1>💻 معرض أعمال المطور المحترف</h1>
            <p>مرحباً بك! استعرض مشاريعي التي قمت بتطويرها بالكامل.</p>
        </header>

        <section class="visitor-form-section">
            <div class="form-title">📝 سجل زوار المعرض (أضف بصمتك)</div>
            <form onsubmit="event.preventDefault(); alert('تم حفظ بياناتك بنجاح في سجل الزوار المطور!');">
                <div class="form-group"><input type="text" placeholder="اسمك الكريم هنا" required></div>
                <div class="form-group"><textarea rows="2" placeholder="اكتب رأيك أو رسالتك للمطور هنا..." required></textarea></div>
                <button type="submit" class="btn-submit">اضغط لحفظ رأيك في لوحة الشرف 💾</button>
            </form>
        </section>

        <main class="projects-grid">
            <article class="project-card">
                <div class="project-icon-title"><span class="project-icon">👋</span><h3 class="project-title">الموقع الترحيبي الشخصي</h3></div>
                <p class="project-desc">صفحة هبوط مميزة ترحب بالزوار بألوان متناسقة وتستعرض المهارات والروابط الشخصية.</p>
                <a href="#" class="project-link">عرض المشروع الترحيبي ←</a>
            </article>

            <article class="project-card">
                <div class="project-icon-title"><span class="project-icon">🔐</span><h3 class="project-title">موقع تسجيل الدخول</h3></div>
                <p class="project-desc">نظام متكامل لتسجيل دخول المستخدمين وإنشاء حسابات جديدة مع حماية وتأمين كلمات المرور.</p>
                <a href="#" class="project-link">عرض صفحة الدخول ←</a>
            </article>

            <article class="project-card">
                <div class="project-icon-title"><span class="project-icon">🗄️</span><h3 class="project-title">موقع تخزين البيانات</h3></div>
                <p class="project-desc">منصة تتيح للمستخدم رفع الملفات والصور وتخزين البيانات السحابية في قواعد بيانات منظمة.</p>
                <a href="#" class="project-link">عرض لوحة البيانات ←</a>
            </article>

            <article class="project-card">
                <div class="project-icon-title"><span class="project-icon">🍔</span><h3 class="project-title">موقع طلبات المطعم</h3></div>
                <p class="project-desc">موقع تفاعلي لعرض قائمة الطعام والأصناف مع إمكانية إضافة الوجبات إلى السلة وطلبها مباشرة.</p>
                <a href="#" class="project-link">تصفح قائمة الطعام ←</a>
            </article>

            <article class="project-card">
                <div class="project-icon-title"><span class="project-icon">🛍️</span><h3 class="project-title">متجر ملابس متكامل</h3></div>
                <p class="project-desc">متجر أزياء إلكتروني حديث لعرض الملابس مع فلاتر لتنقية وتحديد المقاسات والأسعار والألوان.</p>
                <a href="#" class="project-link">زيارة متجر الملابس ←</a>
            </article>
        </main>

        <footer class="portfolio-footer">
            <p>جميع الحقوق محفوظة © 2026 | تم التشغيل والتطوير عبر Pydroid 3</p>
        </footer>
    </div>
</body>
</html>
"""

# حفظ الملف في مسار التطبيق الحالي
file_name = "index.html"
with open(file_name, "w", encoding="utf-8") as f:
    f.write(html_content)

# إعدادات السيرفر
PORT = 9090
class MyHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass # إخفاء السجلات الزائدة للحفاظ على نظافة الشاشة السوداء

server = HTTPServer(('127.0.0.1', PORT), MyHandler)

print("="*40)
print("🚀 [تم تشغيل خادم معرض الأعمال بنجاح]")
print("="*40)
print(f"الرابط المباشر للموقع هو:")
print(f"http://127.0.0.1:{PORT}")
print("="*40)
print("💡 خطوة أخيرة لرؤية موقعك:")
print("1. افتح متصفح جوجل كروم على هاتفك.")
print(f"2. اكتب في خانة البحث فوق: http://127.0.0.1:{PORT}")
print("3. اضغط انطلاق لترى معرضك الرائع يعمل!")
print("="*40)
print("(اضغط على زر الإيقاف في التطبيق عندما تنتهي لغلق السيرفر)")

# محاولة فتح المتصفح تلقائياً بعد ثانية واحدة
time.sleep(1)
webbrowser.open(f"http://127.0.0.1:{PORT}")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\n[تم إيقاف السيرفر بنجاح]")