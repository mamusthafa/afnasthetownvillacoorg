#!/usr/bin/env python3
"""
THE TOWN VILLA COORG - Complete Website Static Generator
Generates all 19 HTML pages, sitemap.xml, robots.txt, webmanifest, and 404 page.
"""

import os
import json

SITE_URL = "https://thetownvillacoorg.com"
PHONE_DISPLAY = "+91 8277268934"
PHONE_RAW = "8277268934"
PHONE_TEL = "tel:+918277268934"
WHATSAPP_LINK = "https://wa.me/918277268934"
WHATSAPP_PREFILLED = "https://wa.me/918277268934?text=Hello%20The%20Town%20Villa%20Coorg%2C%20I%20would%20like%20to%20enquire%20about%20villa%20availability."

def load_template(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

header_template = load_template('components/header.html')
footer_template = load_template('components/footer.html')

def render_header(root_path="", active_tab=""):
    h = header_template.replace("{{ROOT}}", root_path)
    tabs = ["HOME", "VILLAS", "AMENITIES", "GALLERY", "PLACES", "ABOUT", "CONTACT", "LOCATION", "FAMILY", "GROUP", "COUPLE", "FAQ", "BLOG"]
    for t in tabs:
        marker = f"{{{{NAV_{t}}}}}"
        if t == active_tab:
            h = h.replace(marker, "active")
        else:
            h = h.replace(marker, "")
    return h

def render_footer(root_path=""):
    return footer_template.replace("{{ROOT}}", root_path)

def render_page(title, description, canonical_slug, body_content, active_tab="", root_path="", schema_json=None):
    canonical_url = f"{SITE_URL}/{canonical_slug}".rstrip('/')
    if canonical_slug == "" or canonical_slug == "index.html":
        canonical_url = f"{SITE_URL}/"

    schema_block = ""
    if schema_json:
        schema_block = f'<script type="application/ld+json">\n{json.dumps(schema_json, indent=2)}\n</script>'

    header_html = render_header(root_path, active_tab)
    footer_html = render_footer(root_path)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical_url}">
  
  <!-- Favicon & Mobile Meta -->
  <link rel="icon" type="image/x-icon" href="{root_path}favicon.ico">
  <link rel="icon" type="image/png" href="{root_path}assets/icons/favicon.png">
  <link rel="manifest" href="{root_path}site.webmanifest">
  <meta name="theme-color" content="#17352B">

  <!-- Open Graph / Social Sharing -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="{SITE_URL}/assets/images/villas/town-villa-coorg-bedroom-suite.jpg">

  <!-- Twitter Meta -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{SITE_URL}/assets/images/villas/town-villa-coorg-bedroom-suite.jpg">

  <!-- Stylesheets -->
  <link rel="stylesheet" href="{root_path}assets/css/style.css">
  <link rel="stylesheet" href="{root_path}assets/css/responsive.css">

  {schema_block}
</head>
<body>
  {header_html}

  <main id="main-content">
    {body_content}
  </main>

  {footer_html}

  <!-- Scripts -->
  <script src="{root_path}assets/js/main.js"></script>
  <script src="{root_path}assets/js/booking.js"></script>
  <script src="{root_path}assets/js/components.js"></script>
  <script src="{root_path}assets/js/gallery.js"></script>
</body>
</html>
"""

# Common Schema
base_business_schema = {
  "@context": "https://schema.org",
  "@type": "BedAndBreakfast",
  "name": "The Town Villa Coorg",
  "image": [
    f"{SITE_URL}/assets/images/villas/town-villa-coorg-bedroom-suite.jpg",
    f"{SITE_URL}/assets/images/villas/town-villa-coorg-living-dining-layout.jpg"
  ],
  "telephone": "+918277268934",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Near Omkareshwara Temple",
    "addressLocality": "Madikeri",
    "addressRegion": "Karnataka",
    "postalCode": "571201",
    "addressCountry": "IN"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 12.4244,
    "longitude": 75.7382
  },
  "url": SITE_URL,
  "priceRange": "$$",
  "amenityFeature": [
    {"@type": "LocationFeatureSpecification", "name": "Free Wi-Fi", "value": True},
    {"@type": "LocationFeatureSpecification", "name": "Attached Bathrooms with Hot Water", "value": True},
    {"@type": "LocationFeatureSpecification", "name": "Power Backup", "value": True},
    {"@type": "LocationFeatureSpecification", "name": "Television", "value": True},
    {"@type": "LocationFeatureSpecification", "name": "Refrigerator", "value": True},
    {"@type": "LocationFeatureSpecification", "name": "Private Living Room", "value": True},
    {"@type": "LocationFeatureSpecification", "name": "Parking Facility", "value": True}
  ],
  "numberOfRooms": 8,
  "checkinTime": "12:00",
  "checkoutTime": "11:00"
}

def render_booking_form(root=""):
    return f"""
    <div class="booking-component" id="booking-enquiry">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 1rem; margin-bottom: 1.5rem;">
        <div>
          <span class="eyebrow">Direct Booking & Enquiries</span>
          <h3 style="margin-top: 0.25rem;">Check Villa Availability</h3>
          <p style="font-size: 0.9rem; color: var(--color-text-muted); margin-top: 0.2rem;">
            Instant WhatsApp confirmation direct with the host • No third-party platform commissions
          </p>
        </div>
        <span class="badge badge-green nights-count-badge">1 Night</span>
      </div>

      <form class="booking-enquiry-form">
        <div class="booking-form-grid">
          <div class="form-group">
            <label class="form-label" for="guest_name">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
              Guest Name
            </label>
            <input type="text" id="guest_name" name="guest_name" class="form-control" placeholder="Your Full Name" required>
          </div>

          <div class="form-group">
            <label class="form-label" for="checkin">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
              Check-In Date
            </label>
            <input type="date" id="checkin" name="checkin" class="form-control" required>
          </div>

          <div class="form-group">
            <label class="form-label" for="checkout">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
              Check-Out Date
            </label>
            <input type="date" id="checkout" name="checkout" class="form-control" required>
          </div>

          <div class="form-group">
            <label class="form-label" for="villas">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
              Villas (2-BR each)
            </label>
            <select id="villas" name="villas" class="form-control">
              <option value="1">1 Villa (2 Bedrooms - 6 to 8 Guests)</option>
              <option value="2">2 Villas (4 Bedrooms - Up to 16 Guests)</option>
              <option value="3">3 Villas (6 Bedrooms - Up to 24 Guests)</option>
              <option value="4">4 Villas (All 8 Bedrooms - Up to 32 Guests)</option>
            </select>
          </div>

          <div class="form-group">
            <label class="form-label" for="guests">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
              Total Guests
            </label>
            <select id="guests" name="guests" class="form-control">
              <option value="2">2 Guests</option>
              <option value="4">4 Guests</option>
              <option value="6" selected>6 Guests</option>
              <option value="8">8 Guests (with extra beds)</option>
              <option value="10">10 Guests</option>
              <option value="12">12 Guests</option>
              <option value="16">16 Guests</option>
              <option value="20">20 Guests</option>
              <option value="24">24 Guests</option>
              <option value="30">30 Guests</option>
              <option value="32">32 Guests (Full Property)</option>
            </select>
          </div>

          <div class="form-group">
            <label class="form-label" for="extra_beds">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 4v16"/><path d="M2 8h18a2 2 0 0 1 2 2v10"/><path d="M2 17h20"/><circle cx="6" cy="8" r="2"/></svg>
              Extra Beds (On Request)
            </label>
            <select id="extra_beds" name="extra_beds" class="form-control">
              <option value="0">0 Extra Beds</option>
              <option value="1">1 Extra Bed</option>
              <option value="2">2 Extra Beds</option>
              <option value="3">3 Extra Beds</option>
              <option value="4">4 Extra Beds</option>
            </select>
          </div>
        </div>

        <div class="booking-notice">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
          <span>Availability and customized tariff will be confirmed immediately over WhatsApp or phone by the homestay manager.</span>
        </div>

        <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
          <button type="submit" class="btn btn-whatsapp btn-lg" style="flex: 2 1 280px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2ZM12.05 20.15C10.57 20.15 9.12 19.76 7.85 19.01L7.55 18.83L4.43 19.65L5.26 16.61L5.06 16.29C4.24 14.99 3.81 13.47 3.81 11.91C3.81 7.37 7.5 3.68 12.05 3.68C14.25 3.68 16.32 4.54 17.88 6.09C19.43 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.59 20.15 12.05 20.15ZM16.57 14.37C16.32 14.25 15.1 13.65 14.87 13.57C14.65 13.48 14.48 13.44 14.32 13.69C14.15 13.94 13.67 14.5 13.52 14.67C13.38 14.83 13.23 14.85 12.98 14.73C12.73 14.6 11.93 14.34 10.98 13.49C10.24 12.83 9.74 12.02 9.59 11.77C9.45 11.52 9.58 11.39 9.7 11.27C9.81 11.16 9.95 10.98 10.08 10.83C10.2 10.68 10.25 10.57 10.33 10.41C10.41 10.24 10.37 10.1 10.31 9.98C10.25 9.85 9.76 8.65 9.55 8.16C9.35 7.68 9.15 7.74 9 7.74H8.53C8.36 7.74 8.09 7.8 7.86 8.05C7.63 8.3 7 8.89 7 10.09C7 11.29 7.88 12.45 8 12.61C8.13 12.78 9.72 15.23 12.16 16.29C12.74 16.54 13.19 16.69 13.54 16.8C14.12 16.99 14.65 16.96 15.07 16.9C15.54 16.83 16.51 16.31 16.71 15.74C16.92 15.17 16.92 14.68 16.85 14.58C16.79 14.47 16.64 14.41 16.39 14.29L16.57 14.37Z"/></svg>
            <span>Enquire on WhatsApp</span>
          </button>
          <a href="{PHONE_TEL}" class="btn btn-outline-dark btn-lg" style="flex: 1 1 200px;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
            <span>Call Host: {PHONE_DISPLAY}</span>
          </a>
        </div>
      </form>
    </div>
    """

def render_lightbox_modal():
    return """
    <div class="lightbox-modal" id="lightbox-modal" role="dialog" aria-modal="true" aria-label="Photo Lightbox">
      <button class="lightbox-close" aria-label="Close Lightbox">&times;</button>
      <button class="lightbox-prev" aria-label="Previous Photo">&#10094;</button>
      <button class="lightbox-next" aria-label="Next Photo">&#10095;</button>
      <div class="lightbox-content">
        <img class="lightbox-img" src="" alt="The Town Villa Coorg Full Photo">
        <div class="lightbox-caption-bar">
          <p class="lightbox-caption-text" style="font-weight: 600; margin-bottom: 0.2rem;"></p>
          <span class="lightbox-counter" style="font-size: 0.85rem; opacity: 0.75;"></span>
        </div>
      </div>
    </div>
    """

def render_amenities_grid():
    amenities = [
        ("2 Bedrooms per Villa", "Spacious master and guest bedrooms with comfortable king & queen beds.", '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 4v16"/><path d="M2 8h18a2 2 0 0 1 2 2v10"/><path d="M2 17h20"/><circle cx="6" cy="8" r="2"/></svg>'),
        ("Private Living Room", "Dedicated hall with comfortable sofa seating, tea table and room fan.", '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="10" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>'),
        ("Dining Area", "Family dining table with chairs for relaxing meals together in privacy.", '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2v20"/><path d="M2 12h20"/></svg>'),
        ("Attached Bathrooms", "Clean modern western bathrooms with continuous 24/7 hot water geysers.", '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 12h16a1 1 0 0 1 1 1v3a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4v-3a1 1 0 0 1 1-1Z"/><path d="M6 12V5a2 2 0 0 1 2-2h1"/></svg>'),
        ("Television in Every Villa", "Wall-mounted LED flatscreen television for entertainment after sightseeing.", '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="15" rx="2" ry="2"/><polyline points="17 2 12 7 7 2"/></svg>'),
        ("High-Speed Wi-Fi", "Complimentary wireless internet to stay connected throughout the property.", '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12.55a11 11 0 0 1 14.08 0"/><path d="M1.42 9a16 16 0 0 1 21.16 0"/><path d="M8.53 16.11a6 6 0 0 1 6.95 0"/><line x1="12" y1="20" x2="12.01" y2="20"/></svg>'),
        ("Refrigerator", "In-villa refrigerator to keep fruits, refreshments, water and medicines cold.", '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="4" y1="10" x2="20" y2="10"/><line x1="8" y1="6" x2="8.01" y2="6"/><line x1="8" y1="14" x2="8.01" y2="14"/></svg>'),
        ("Power Backup Inverter", "Dedicated power backup inverter so lights, fans and Wi-Fi remain uninterrupted.", '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>'),
        ("Hot Water Geyser", "Instant hot water available round-the-clock for refreshing baths in cool Coorg weather.", '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/></svg>'),
        ("Vehicle Parking", "Safe, dedicated parking space on premises for cars and traveller vans.", '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="5" width="20" height="14" rx="2"/><path d="M9 17V7h4a3 3 0 0 1 0 6H9"/></svg>'),
        ("Extra Bed Available", "1 additional bed per bedroom available on request for extended groups.", '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 7h18v10H3z"/><path d="M8 7v10"/><path d="M16 7v10"/></svg>'),
        ("6–8 Guests Capacity", "Comfortably houses large family groups with total capacity up to 32 guests.", '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>')
    ]

    cards_html = ""
    for title, desc, icon in amenities:
        cards_html += f"""
        <div class="amenity-card">
          <div class="amenity-icon-box">
            {icon}
          </div>
          <div class="amenity-info">
            <h4>{title}</h4>
            <p>{desc}</p>
          </div>
        </div>
        """
    return f'<div class="amenities-grid">{cards_html}</div>'

def render_faq_accordions():
    faqs = [
        ("Where is The Town Villa Coorg located in Madikeri?",
         "The Town Villa Coorg is situated in central Madikeri, conveniently close to the famous Omkareshwara Temple. This prime location places you within walking distance or a short 5-minute drive to Madikeri Fort, Raja's Seat, the local market, and prominent dining establishments."),
        ("How many guests can stay in each villa?",
         "Each villa features 2 spacious private bedrooms, a private living hall, a dining area, and attached bathrooms. It comfortably accommodates 6 guests, and up to 8 guests with optional extra beds. With 4 total villas, our property can host large groups and families of 24 to 32 guests."),
        ("What amenities are included with each villa?",
         "Every villa includes high-speed Wi-Fi, LED television, a refrigerator, private dining room, power backup inverter, 24/7 hot water geyser, attached modern bathrooms, and vehicle parking. Fresh linens and bath towels are provided upon arrival."),
        ("Are extra beds available for larger families or groups?",
         "Yes, we can provide 1 additional comfortable bed per bedroom upon request to conveniently accommodate children or extra adults."),
        ("Is vehicle parking available on the property?",
         "Yes, we have safe parking space on premises for guest cars and group traveller vans, giving you peace of mind during your stay in Madikeri."),
        ("How do we check availability and confirm a booking?",
         "Booking is direct, fast, and transparent. Simply call us at +91 8277268934 or click our WhatsApp enquiry buttons with your dates and guest numbers. We will instantly verify availability and provide the best direct host rate with no middleman markups.")
    ]

    faq_html = ""
    for q, a in faqs:
        faq_html += f"""
        <div class="faq-item">
          <button class="faq-question">
            <span>{q}</span>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer">
            <p>{a}</p>
          </div>
        </div>
        """
    return f'<div class="faq-list">{faq_html}</div>'

print("Helper builders ready.")
