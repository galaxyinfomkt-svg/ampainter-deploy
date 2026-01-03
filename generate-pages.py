import os

# Cities within 15 miles of Hudson, MA
cities = [
    {"name": "Hudson", "state": "MA", "county": "Middlesex"},
    {"name": "Marlborough", "state": "MA", "county": "Middlesex"},
    {"name": "Stow", "state": "MA", "county": "Middlesex"},
    {"name": "Bolton", "state": "MA", "county": "Worcester"},
    {"name": "Berlin", "state": "MA", "county": "Worcester"},
    {"name": "Northborough", "state": "MA", "county": "Worcester"},
    {"name": "Southborough", "state": "MA", "county": "Worcester"},
    {"name": "Westborough", "state": "MA", "county": "Worcester"},
    {"name": "Shrewsbury", "state": "MA", "county": "Worcester"},
    {"name": "Boylston", "state": "MA", "county": "Worcester"},
    {"name": "Clinton", "state": "MA", "county": "Worcester"},
    {"name": "Lancaster", "state": "MA", "county": "Worcester"},
    {"name": "Sterling", "state": "MA", "county": "Worcester"},
    {"name": "Maynard", "state": "MA", "county": "Middlesex"},
    {"name": "Sudbury", "state": "MA", "county": "Middlesex"},
    {"name": "Wayland", "state": "MA", "county": "Middlesex"},
    {"name": "Framingham", "state": "MA", "county": "Middlesex"},
    {"name": "Natick", "state": "MA", "county": "Middlesex"},
    {"name": "Ashland", "state": "MA", "county": "Middlesex"},
    {"name": "Hopkinton", "state": "MA", "county": "Middlesex"},
    {"name": "Holliston", "state": "MA", "county": "Middlesex"},
    {"name": "Milford", "state": "MA", "county": "Worcester"},
    {"name": "Grafton", "state": "MA", "county": "Worcester"},
    {"name": "Upton", "state": "MA", "county": "Worcester"},
    {"name": "Mendon", "state": "MA", "county": "Worcester"},
    {"name": "Hopedale", "state": "MA", "county": "Worcester"},
    {"name": "Bellingham", "state": "MA", "county": "Norfolk"},
    {"name": "Medway", "state": "MA", "county": "Norfolk"},
    {"name": "Franklin", "state": "MA", "county": "Norfolk"},
    {"name": "Acton", "state": "MA", "county": "Middlesex"},
    {"name": "Concord", "state": "MA", "county": "Middlesex"},
    {"name": "Lincoln", "state": "MA", "county": "Middlesex"},
    {"name": "Weston", "state": "MA", "county": "Middlesex"},
    {"name": "Wellesley", "state": "MA", "county": "Norfolk"},
    {"name": "Needham", "state": "MA", "county": "Norfolk"},
    {"name": "Dover", "state": "MA", "county": "Norfolk"},
    {"name": "Sherborn", "state": "MA", "county": "Middlesex"},
    {"name": "Millis", "state": "MA", "county": "Norfolk"},
    {"name": "Norfolk", "state": "MA", "county": "Norfolk"},
    {"name": "Wrentham", "state": "MA", "county": "Norfolk"},
]

services = [
    {"name": "Interior Painting", "slug": "interior-painting", "desc": "Transform your indoor spaces with expert interior painting services"},
    {"name": "Exterior Painting", "slug": "exterior-painting", "desc": "Protect and beautify your home's exterior with weather-resistant finishes"},
    {"name": "Cabinet Refinishing", "slug": "cabinet-refinishing", "desc": "Save 50-70% with professional cabinet painting and refinishing"},
    {"name": "Deck Staining", "slug": "deck-staining", "desc": "Protect and enhance your outdoor deck with professional staining"},
    {"name": "Commercial Painting", "slug": "commercial-painting", "desc": "Professional painting services for businesses and commercial properties"},
    {"name": "Pressure Washing", "slug": "pressure-washing", "desc": "Restore your property's appearance with professional power washing"},
]

# Create directories
os.makedirs("locations", exist_ok=True)
for service in services:
    os.makedirs(f"locations/{service['slug']}", exist_ok=True)

def get_city_page(city):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Painter Near Me in {city["name"]}, {city["state"]} | A&M Painter Inc</title>
    <meta name="description" content="Looking for a painter near me in {city["name"]}, {city["state"]}? A&M Painter Inc offers professional painting services in {city["county"]} County. Interior, exterior, cabinet refinishing. 32+ years experience. Free estimates!">
    <meta name="keywords" content="painter near me {city["name"]}, {city["name"]} painters, painting company {city["name"]} MA, house painters {city["name"]}, {city["county"]} County painters">
    <link rel="canonical" href="https://ampainterinc.com/locations/{city["name"].lower().replace(" ", "-")}.html">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        primary: '#E10600',
                        secondary: '#0A1F44',
                    }}
                }}
            }}
        }}
    </script>
</head>
<body class="font-sans">
    <!-- Nav -->
    <nav class="fixed w-full z-50 bg-white shadow-lg">
        <div class="container mx-auto px-4 py-4 flex justify-between items-center">
            <a href="../index.html">
                <img src="https://storage.googleapis.com/msgsndr/npwVVdTpo5dMM8CCSeCT/media/6939d7e1f6cae99fddea0e51.png" alt="A&M Painter Inc" class="h-12">
            </a>
            <a href="tel:5086310469" class="bg-primary text-white px-6 py-3 rounded-full font-bold hover:bg-red-700">(508) 631-0469</a>
        </div>
    </nav>

    <!-- Hero -->
    <section class="pt-24 pb-16 bg-gradient-to-br from-secondary to-blue-900 text-white">
        <div class="container mx-auto px-4">
            <div class="max-w-4xl mx-auto text-center">
                <span class="bg-primary/20 px-4 py-2 rounded-full text-sm font-semibold mb-4 inline-block">Painter Near Me in {city["name"]}</span>
                <h1 class="text-4xl md:text-6xl font-black mb-6">Professional Painting Services in {city["name"]}, {city["state"]}</h1>
                <p class="text-xl text-gray-200 mb-8">Trusted by homeowners in {city["county"]} County for over 32 years. Licensed, insured, and committed to excellence.</p>
                <div class="flex flex-col sm:flex-row gap-4 justify-center">
                    <a href="#quote" class="bg-primary text-white px-8 py-4 rounded-full font-bold text-lg hover:bg-red-700">Get Free Estimate</a>
                    <a href="tel:5086310469" class="border-2 border-white px-8 py-4 rounded-full font-bold text-lg hover:bg-white hover:text-secondary">(508) 631-0469</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Why Choose Us -->
    <section class="py-20 bg-white">
        <div class="container mx-auto px-4">
            <div class="max-w-4xl mx-auto">
                <h2 class="text-3xl md:text-4xl font-black text-secondary mb-8 text-center">Why {city["name"]} Homeowners Choose A&M Painter Inc</h2>

                <div class="prose prose-lg max-w-none text-gray-700 space-y-6">
                    <p>When residents of <strong>{city["name"]}, Massachusetts</strong> search for a <strong>painter near me</strong>, they need a contractor who understands local homes and delivers exceptional results. A&M Painter Inc has been the trusted choice for <strong>painting services in {city["name"]}</strong> and throughout {city["county"]} County for over three decades.</p>

                    <p>Our team of professional <strong>{city["name"]} painters</strong> brings expertise, reliability, and attention to detail to every project. Whether you need interior painting to refresh your living spaces, exterior painting to boost curb appeal, or cabinet refinishing to transform your kitchen, we deliver results that exceed expectations.</p>

                    <p>As a locally owned and operated <strong>painting company near {city["name"]}</strong>, we understand the unique characteristics of homes in {city["county"]} County. From historic New England architecture to modern construction, we have the experience and skills to handle any painting project with precision and care.</p>
                </div>

                <div class="grid md:grid-cols-3 gap-8 mt-12">
                    <div class="text-center p-6 bg-gray-50 rounded-2xl">
                        <div class="text-4xl font-black text-primary mb-2">32+</div>
                        <div class="text-gray-600">Years Experience</div>
                    </div>
                    <div class="text-center p-6 bg-gray-50 rounded-2xl">
                        <div class="text-4xl font-black text-primary mb-2">$2M</div>
                        <div class="text-gray-600">Fully Insured</div>
                    </div>
                    <div class="text-center p-6 bg-gray-50 rounded-2xl">
                        <div class="text-4xl font-black text-primary mb-2">5.0</div>
                        <div class="text-gray-600">Star Rating</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Services -->
    <section class="py-20 bg-gray-50">
        <div class="container mx-auto px-4">
            <h2 class="text-3xl md:text-4xl font-black text-secondary mb-12 text-center">Our Painting Services in {city["name"]}</h2>
            <div class="grid md:grid-cols-3 gap-8 max-w-6xl mx-auto">
                <a href="{city["name"].lower().replace(" ", "-")}/interior-painting.html" class="bg-white p-8 rounded-2xl shadow-lg hover:shadow-xl transition-shadow">
                    <h3 class="text-xl font-bold text-secondary mb-3">Interior Painting</h3>
                    <p class="text-gray-600 mb-4">Expert wall, ceiling, and trim painting for homes in {city["name"]}.</p>
                    <span class="text-primary font-semibold">Learn More →</span>
                </a>
                <a href="{city["name"].lower().replace(" ", "-")}/exterior-painting.html" class="bg-white p-8 rounded-2xl shadow-lg hover:shadow-xl transition-shadow">
                    <h3 class="text-xl font-bold text-secondary mb-3">Exterior Painting</h3>
                    <p class="text-gray-600 mb-4">Weather-resistant exterior painting for {city["name"]} homes.</p>
                    <span class="text-primary font-semibold">Learn More →</span>
                </a>
                <a href="{city["name"].lower().replace(" ", "-")}/cabinet-refinishing.html" class="bg-white p-8 rounded-2xl shadow-lg hover:shadow-xl transition-shadow">
                    <h3 class="text-xl font-bold text-secondary mb-3">Cabinet Refinishing</h3>
                    <p class="text-gray-600 mb-4">Transform your kitchen cabinets for a fraction of replacement cost.</p>
                    <span class="text-primary font-semibold">Learn More →</span>
                </a>
            </div>
        </div>
    </section>

    <!-- Local SEO Content -->
    <section class="py-20 bg-white">
        <div class="container mx-auto px-4">
            <div class="max-w-4xl mx-auto">
                <h2 class="text-3xl font-black text-secondary mb-8">Serving {city["name"]} and {city["county"]} County</h2>
                <div class="prose prose-lg text-gray-700 space-y-6">
                    <p>A&M Painter Inc proudly serves <strong>{city["name"]}, {city["state"]}</strong> and all surrounding communities in {city["county"]} County. Our local painting contractors are familiar with the area and committed to providing prompt, professional service to homeowners and businesses throughout the region.</p>

                    <p>When you hire A&M Painter Inc as your <strong>{city["name"]} painting contractor</strong>, you're choosing a company that values quality, integrity, and customer satisfaction above all else. We treat every home as if it were our own, ensuring meticulous preparation, premium materials, and flawless execution on every project.</p>

                    <h3 class="text-2xl font-bold text-secondary mt-8">What Sets Us Apart in {city["name"]}</h3>
                    <ul class="list-disc pl-6 space-y-2">
                        <li><strong>Local Expertise:</strong> We understand {city["name"]} homes and local conditions</li>
                        <li><strong>Premium Materials:</strong> Benjamin Moore, Sherwin-Williams, and other top brands</li>
                        <li><strong>Detailed Preparation:</strong> Proper prep for lasting results</li>
                        <li><strong>Clean Work Sites:</strong> We respect your home and property</li>
                        <li><strong>Clear Communication:</strong> You'll always know project status</li>
                        <li><strong>Satisfaction Guarantee:</strong> We're not done until you're happy</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- FAQ -->
    <section class="py-20 bg-gray-50">
        <div class="container mx-auto px-4">
            <div class="max-w-4xl mx-auto">
                <h2 class="text-3xl font-black text-secondary mb-12 text-center">Frequently Asked Questions - Painting in {city["name"]}</h2>
                <div class="space-y-6">
                    <div class="bg-white p-8 rounded-2xl shadow">
                        <h3 class="text-xl font-bold text-secondary mb-3">How much does painting cost in {city["name"]}?</h3>
                        <p class="text-gray-700">Interior painting in {city["name"]} typically ranges from $300-$800 per room. Exterior painting averages $3,000-$8,000 for a standard home. We provide free, detailed estimates with transparent pricing.</p>
                    </div>
                    <div class="bg-white p-8 rounded-2xl shadow">
                        <h3 class="text-xl font-bold text-secondary mb-3">Do you serve all of {city["county"]} County?</h3>
                        <p class="text-gray-700">Yes! We serve {city["name"]} and all surrounding communities in {city["county"]} County and beyond. Contact us to confirm service in your specific area.</p>
                    </div>
                    <div class="bg-white p-8 rounded-2xl shadow">
                        <h3 class="text-xl font-bold text-secondary mb-3">Are you licensed and insured?</h3>
                        <p class="text-gray-700">Absolutely. A&M Painter Inc is fully licensed and carries $2 million in liability insurance for your protection and peace of mind.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Quote Form -->
    <section id="quote" class="py-20 bg-secondary">
        <div class="container mx-auto px-4">
            <div class="max-w-2xl mx-auto text-center">
                <h2 class="text-3xl font-black text-white mb-4">Get Your Free Quote in {city["name"]}</h2>
                <p class="text-gray-300 mb-8">Professional estimate within 24 hours</p>
                <div class="bg-white rounded-2xl p-6">
                    <iframe
                        src="https://api.leadconnectorhq.com/widget/form/c7kM3Sd6fSoWqz1RZIOK"
                        style="width:100%;height:450px;border:none;"
                        id="inline-c7kM3Sd6fSoWqz1RZIOK"
                        data-layout='{{"id":"INLINE"}}'
                        data-trigger-type="alwaysShow"
                        data-trigger-value=""
                        data-activation-type="alwaysActivated"
                        data-activation-value=""
                        data-deactivation-type="neverDeactivate"
                        data-deactivation-value=""
                        data-form-name="AM Painter - Quote Form"
                        data-height="450"
                        data-layout-iframe-id="inline-c7kM3Sd6fSoWqz1RZIOK"
                        data-form-id="c7kM3Sd6fSoWqz1RZIOK"
                        title="AM Painter - Quote Form">
                    </iframe>
                    <script src="https://link.msgsndr.com/js/form_embed.js"></script>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA -->
    <section class="py-16 bg-primary">
        <div class="container mx-auto px-4 text-center">
            <h2 class="text-3xl font-black text-white mb-6">Ready to Transform Your {city["name"]} Home?</h2>
            <a href="tel:5086310469" class="inline-flex items-center gap-3 bg-white text-secondary px-8 py-4 rounded-full font-bold text-xl hover:bg-gray-100">
                Call (508) 631-0469
            </a>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-secondary text-white py-12">
        <div class="container mx-auto px-4">
            <div class="grid md:grid-cols-4 gap-8">
                <div>
                    <img src="https://storage.googleapis.com/msgsndr/npwVVdTpo5dMM8CCSeCT/media/6939d7e1f6cae99fddea0e51.png" alt="A&M Painter Inc" class="h-12 mb-4">
                    <p class="text-gray-400">Professional painting services in {city["name"]}, MA and surrounding areas.</p>
                </div>
                <div>
                    <h4 class="font-bold mb-4">Services</h4>
                    <ul class="space-y-2 text-gray-400">
                        <li><a href="../services/interior-painting.html" class="hover:text-white">Interior Painting</a></li>
                        <li><a href="../services/exterior-painting.html" class="hover:text-white">Exterior Painting</a></li>
                        <li><a href="../services/cabinet-refinishing.html" class="hover:text-white">Cabinet Refinishing</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="font-bold mb-4">Contact</h4>
                    <ul class="space-y-2 text-gray-400">
                        <li>(508) 631-0469</li>
                        <li>info@ampainterinc.com</li>
                        <li>74 Broad St, Hudson, MA</li>
                    </ul>
                </div>
                <div>
                    <h4 class="font-bold mb-4">Hours</h4>
                    <ul class="space-y-2 text-gray-400">
                        <li>Mon-Fri: 7AM - 6PM</li>
                        <li>Sat: 8AM - 2PM</li>
                        <li>Sun: Closed</li>
                    </ul>
                </div>
            </div>
            <div class="border-t border-gray-700 mt-8 pt-8 text-center text-gray-400">
                <p>&copy; 2024 A&M Painter Inc. All rights reserved.</p>
            </div>
        </div>
    </footer>
</body>
</html>'''

def get_city_service_page(city, service):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{service["name"]} in {city["name"]}, {city["state"]} | Painter Near Me | A&M Painter Inc</title>
    <meta name="description" content="Professional {service["name"].lower()} services in {city["name"]}, {city["state"]}. {service["desc"]}. 32+ years experience, fully insured. Free estimates!">
    <meta name="keywords" content="{service["name"].lower()} {city["name"]}, {service["slug"]} near me, {city["name"]} {service["slug"]}, {city["county"]} County painters">
    <link rel="canonical" href="https://ampainterinc.com/locations/{city["name"].lower().replace(" ", "-")}/{service["slug"]}.html">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        primary: '#E10600',
                        secondary: '#0A1F44',
                    }}
                }}
            }}
        }}
    </script>
</head>
<body class="font-sans">
    <!-- Nav -->
    <nav class="fixed w-full z-50 bg-white shadow-lg">
        <div class="container mx-auto px-4 py-4 flex justify-between items-center">
            <a href="../../index.html">
                <img src="https://storage.googleapis.com/msgsndr/npwVVdTpo5dMM8CCSeCT/media/6939d7e1f6cae99fddea0e51.png" alt="A&M Painter Inc" class="h-12">
            </a>
            <a href="tel:5086310469" class="bg-primary text-white px-6 py-3 rounded-full font-bold hover:bg-red-700">(508) 631-0469</a>
        </div>
    </nav>

    <!-- Hero -->
    <section class="pt-24 pb-16 bg-gradient-to-br from-secondary to-blue-900 text-white">
        <div class="container mx-auto px-4">
            <div class="max-w-4xl mx-auto text-center">
                <span class="bg-primary/20 px-4 py-2 rounded-full text-sm font-semibold mb-4 inline-block">{service["name"]} Near Me</span>
                <h1 class="text-4xl md:text-5xl font-black mb-6">Professional {service["name"]} in {city["name"]}, {city["state"]}</h1>
                <p class="text-xl text-gray-200 mb-8">{service["desc"]}. Serving {city["name"]} and {city["county"]} County with 32+ years of excellence.</p>
                <div class="flex flex-col sm:flex-row gap-4 justify-center">
                    <a href="#quote" class="bg-primary text-white px-8 py-4 rounded-full font-bold text-lg hover:bg-red-700">Get Free Estimate</a>
                    <a href="tel:5086310469" class="border-2 border-white px-8 py-4 rounded-full font-bold text-lg hover:bg-white hover:text-secondary">(508) 631-0469</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Content -->
    <section class="py-20 bg-white">
        <div class="container mx-auto px-4">
            <div class="max-w-4xl mx-auto">
                <h2 class="text-3xl font-black text-secondary mb-8">Expert {service["name"]} Services in {city["name"]}</h2>
                <div class="prose prose-lg text-gray-700 space-y-6">
                    <p>Looking for professional <strong>{service["name"].lower()} near me</strong> in {city["name"]}, Massachusetts? A&M Painter Inc is your trusted local contractor specializing in {service["name"].lower()} throughout {city["county"]} County. With over 32 years of experience, our skilled professionals deliver superior craftsmanship on every project.</p>

                    <p>Whether you're a homeowner looking to refresh your property or a business owner maintaining your commercial space, our <strong>{service["name"].lower()} services in {city["name"]}</strong> are designed to exceed your expectations. We use premium materials and proven techniques to ensure lasting, beautiful results.</p>

                    <p>As your local <strong>{city["name"]} {service["slug"].replace("-", " ")} contractor</strong>, we understand the unique needs of properties in {city["county"]} County. Our team delivers personalized service, clear communication, and results that enhance your property's value and appeal.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Why Choose Us -->
    <section class="py-20 bg-gray-50">
        <div class="container mx-auto px-4">
            <div class="max-w-4xl mx-auto">
                <h2 class="text-3xl font-black text-secondary mb-12 text-center">Why Choose A&M for {service["name"]} in {city["name"]}?</h2>
                <div class="grid md:grid-cols-2 gap-8">
                    <div class="bg-white p-6 rounded-xl shadow">
                        <h3 class="font-bold text-secondary mb-2">32+ Years Experience</h3>
                        <p class="text-gray-600">Decades of expertise serving {city["county"]} County homeowners.</p>
                    </div>
                    <div class="bg-white p-6 rounded-xl shadow">
                        <h3 class="font-bold text-secondary mb-2">$2M Insurance</h3>
                        <p class="text-gray-600">Fully licensed and insured for your complete protection.</p>
                    </div>
                    <div class="bg-white p-6 rounded-xl shadow">
                        <h3 class="font-bold text-secondary mb-2">Premium Materials</h3>
                        <p class="text-gray-600">We use only top-quality paints and materials.</p>
                    </div>
                    <div class="bg-white p-6 rounded-xl shadow">
                        <h3 class="font-bold text-secondary mb-2">Satisfaction Guarantee</h3>
                        <p class="text-gray-600">We're not finished until you're completely satisfied.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Process -->
    <section class="py-20 bg-white">
        <div class="container mx-auto px-4">
            <h2 class="text-3xl font-black text-secondary mb-12 text-center">Our {service["name"]} Process</h2>
            <div class="grid md:grid-cols-4 gap-8 max-w-5xl mx-auto">
                <div class="text-center">
                    <div class="w-12 h-12 bg-primary text-white rounded-full flex items-center justify-center mx-auto mb-4 font-bold">1</div>
                    <h3 class="font-bold text-secondary mb-2">Free Quote</h3>
                    <p class="text-gray-600 text-sm">Detailed estimate with no obligation.</p>
                </div>
                <div class="text-center">
                    <div class="w-12 h-12 bg-primary text-white rounded-full flex items-center justify-center mx-auto mb-4 font-bold">2</div>
                    <h3 class="font-bold text-secondary mb-2">Preparation</h3>
                    <p class="text-gray-600 text-sm">Thorough prep for lasting results.</p>
                </div>
                <div class="text-center">
                    <div class="w-12 h-12 bg-primary text-white rounded-full flex items-center justify-center mx-auto mb-4 font-bold">3</div>
                    <h3 class="font-bold text-secondary mb-2">Expert Work</h3>
                    <p class="text-gray-600 text-sm">Professional application by skilled craftsmen.</p>
                </div>
                <div class="text-center">
                    <div class="w-12 h-12 bg-primary text-white rounded-full flex items-center justify-center mx-auto mb-4 font-bold">4</div>
                    <h3 class="font-bold text-secondary mb-2">Final Review</h3>
                    <p class="text-gray-600 text-sm">Walkthrough to ensure your satisfaction.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Quote Form -->
    <section id="quote" class="py-20 bg-secondary">
        <div class="container mx-auto px-4">
            <div class="max-w-2xl mx-auto text-center">
                <h2 class="text-3xl font-black text-white mb-4">Get Your Free {service["name"]} Quote</h2>
                <p class="text-gray-300 mb-8">Professional estimate for your {city["name"]} home</p>
                <div class="bg-white rounded-2xl p-6">
                    <iframe
                        src="https://api.leadconnectorhq.com/widget/form/c7kM3Sd6fSoWqz1RZIOK"
                        style="width:100%;height:450px;border:none;"
                        id="inline-c7kM3Sd6fSoWqz1RZIOK"
                        data-layout='{{"id":"INLINE"}}'
                        data-trigger-type="alwaysShow"
                        data-trigger-value=""
                        data-activation-type="alwaysActivated"
                        data-activation-value=""
                        data-deactivation-type="neverDeactivate"
                        data-deactivation-value=""
                        data-form-name="AM Painter - Quote Form"
                        data-height="450"
                        data-layout-iframe-id="inline-c7kM3Sd6fSoWqz1RZIOK"
                        data-form-id="c7kM3Sd6fSoWqz1RZIOK"
                        title="AM Painter - Quote Form">
                    </iframe>
                    <script src="https://link.msgsndr.com/js/form_embed.js"></script>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA -->
    <section class="py-16 bg-primary">
        <div class="container mx-auto px-4 text-center">
            <h2 class="text-3xl font-black text-white mb-6">Ready for {service["name"]} in {city["name"]}?</h2>
            <a href="tel:5086310469" class="inline-flex items-center gap-3 bg-white text-secondary px-8 py-4 rounded-full font-bold text-xl hover:bg-gray-100">
                Call (508) 631-0469
            </a>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-secondary text-white py-12">
        <div class="container mx-auto px-4 text-center">
            <p class="text-gray-400">&copy; 2024 A&M Painter Inc. Professional {service["name"]} in {city["name"]}, MA.</p>
        </div>
    </footer>
</body>
</html>'''

# Generate city pages
print("Generating city pages...")
for city in cities:
    filename = f"locations/{city['name'].lower().replace(' ', '-')}.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(get_city_page(city))
    print(f"  Created: {filename}")

    # Create city subfolder and service pages
    city_folder = f"locations/{city['name'].lower().replace(' ', '-')}"
    os.makedirs(city_folder, exist_ok=True)

    for service in services:
        service_filename = f"{city_folder}/{service['slug']}.html"
        with open(service_filename, 'w', encoding='utf-8') as f:
            f.write(get_city_service_page(city, service))

print(f"\nGenerated {len(cities)} city pages")
print(f"Generated {len(cities) * len(services)} city+service pages")
print(f"Total pages: {len(cities) + len(cities) * len(services)}")
