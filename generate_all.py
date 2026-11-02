#!/usr/bin/env python3
"""
COORG VILLA - Complete Page Builder
Generates all 19 HTML pages + sitemap.xml + robots.txt + manifest
"""

import os
import json
from build_site import (
    SITE_URL, PHONE_DISPLAY, PHONE_RAW, PHONE_TEL, WHATSAPP_LINK, WHATSAPP_PREFILLED,
    render_page, render_booking_form, render_lightbox_modal, render_amenities_grid,
    render_faq_accordions, base_business_schema
)

def build_homepage():
    body = f"""
    <!-- SECTION 01: HERO BANNER -->
    <section class="hero-section">
      <div class="hero-background">
        <img src="assets/images/bedrooms/town-villa-coorg-bedroom-spacious.jpg" alt="Coorg Villa Bedroom Suite" fetchpriority="high">
      </div>
      <div class="hero-overlay"></div>
      <div class="container hero-content">
        <div class="hero-tagline">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
          Madikeri • Near Omkareshwara Temple
        </div>
        <h1 class="hero-title">Homestay in Madikeri, Coorg – Coorg Villa</h1>
        <p class="hero-subtitle">
          Spacious 2-bedroom villas for families, groups and couples, conveniently located near Omkareshwara Temple in Madikeri.
        </p>
        <div class="hero-cta-group">
          <a href="villas.html" class="btn btn-gold btn-lg">Explore Our Villas &rarr;</a>
          <a href="{WHATSAPP_PREFILLED}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp btn-lg">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2ZM12.05 20.15C10.57 20.15 9.12 19.76 7.85 19.01L7.55 18.83L4.43 19.65L5.26 16.61L5.06 16.29C4.24 14.99 3.81 13.47 3.81 11.91C3.81 7.37 7.5 3.68 12.05 3.68C14.25 3.68 16.32 4.54 17.88 6.09C19.43 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.59 20.15 12.05 20.15ZM16.57 14.37C16.32 14.25 15.1 13.65 14.87 13.57C14.65 13.48 14.48 13.44 14.32 13.69C14.15 13.94 13.67 14.5 13.52 14.67C13.38 14.83 13.23 14.85 12.98 14.73C12.73 14.6 11.93 14.34 10.98 13.49C10.24 12.83 9.74 12.02 9.59 11.77C9.45 11.52 9.58 11.39 9.7 11.27C9.81 11.16 9.95 10.98 10.08 10.83C10.2 10.68 10.25 10.57 10.33 10.41C10.41 10.24 10.37 10.1 10.31 9.98C10.25 9.85 9.76 8.65 9.55 8.16C9.35 7.68 9.15 7.74 9 7.74H8.53C8.36 7.74 8.09 7.8 7.86 8.05C7.63 8.3 7 8.89 7 10.09C7 11.29 7.88 12.45 8 12.61C8.13 12.78 9.72 15.23 12.16 16.29C12.74 16.54 13.19 16.69 13.54 16.8C14.12 16.99 14.65 16.96 15.07 16.9C15.54 16.83 16.51 16.31 16.71 15.74C16.92 15.17 16.92 14.68 16.85 14.58C16.79 14.47 16.64 14.41 16.39 14.29L16.57 14.37Z"/></svg>
            <span>Book via WhatsApp</span>
          </a>
          <a href="{PHONE_TEL}" class="btn btn-outline-light btn-lg">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
            <span>Call Host: {PHONE_DISPLAY}</span>
          </a>
        </div>
      </div>
    </section>

    <!-- QUICK HIGHLIGHTS STRIP -->
    <div class="container hero-highlights">
      <div class="highlights-card">
        <div class="highlight-item">
          <div class="highlight-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
          </div>
          <div>
            <div class="highlight-title">4 Spacious Villas</div>
            <div class="highlight-sub">2 Bedrooms each</div>
          </div>
        </div>

        <div class="highlight-item">
          <div class="highlight-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
          </div>
          <div>
            <div class="highlight-title">6–8 Guests / Villa</div>
            <div class="highlight-sub">Up to 32 total capacity</div>
          </div>
        </div>

        <div class="highlight-item">
          <div class="highlight-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
          </div>
          <div>
            <div class="highlight-title">Power Backup & Wi-Fi</div>
            <div class="highlight-sub">Uninterrupted comfort</div>
          </div>
        </div>

        <div class="highlight-item">
          <div class="highlight-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
          </div>
          <div>
            <div class="highlight-title">Near Omkareshwara</div>
            <div class="highlight-sub">Central Madikeri town</div>
          </div>
        </div>
      </div>
    </div>

    <!-- SECTION 02: WELCOME INTRODUCTION -->
    <section class="section" id="welcome">
      <div class="container">
        <div class="grid-2" style="align-items: center; gap: 3.5rem;">
          <div>
            <span class="eyebrow">Madikeri Homestay</span>
            <h2>Welcome to Coorg Villa</h2>
            <p style="margin-top: 1.25rem;">
              Nestled right in the heart of Madikeri, Coorg Villa provides the ideal blend of homely warmth, private villa convenience, and unbeatable location. Unlike cramped hotel rooms where families are split across corridors, each of our four distinct villas gives you the luxury of an entire home.
            </p>
            <p>
              With two spacious private bedrooms, an independent living hall, dining space, modern attached bathrooms, and secure parking, you can relax together after an exciting day touring Coorg's misty hills and fragrant coffee estates.
            </p>
            <div style="display: flex; gap: 1rem; margin-top: 2rem; flex-wrap: wrap;">
              <a href="about.html" class="btn btn-primary">Learn More About Us &rarr;</a>
              <a href="location.html" class="btn btn-outline-dark">Explore Our Location</a>
            </div>
          </div>
          <div style="position: relative;">
            <div class="card-img-wrap" style="border-radius: var(--radius-lg); aspect-ratio: 4/3; box-shadow: var(--shadow-lg);">
              <img src="assets/images/villas/town-villa-coorg-living-dining-layout.jpg" alt="Coorg Villa Living & Dining Interior">
            </div>
            <div style="position: absolute; bottom: -1.5rem; right: -1rem; background: var(--color-surface); padding: 1.25rem 1.5rem; border-radius: var(--radius-md); box-shadow: var(--shadow-md); border-left: 4px solid var(--color-accent); max-width: 240px;">
              <strong style="color: var(--color-primary); display: block; font-size: 1.1rem; font-family: var(--font-heading);">Prime Landmark</strong>
              <span style="font-size: 0.85rem; color: var(--color-text-muted);">Steps away from Madikeri's historic Omkareshwara Temple</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 03: OUR SPACIOUS VILLAS -->
    <section class="section" style="background-color: var(--color-surface);" id="villas">
      <div class="container">
        <div class="section-header">
          <span class="eyebrow">Accommodation Overview</span>
          <h2>Stay Together in Our 2-Bedroom Villas</h2>
          <p class="section-subtitle">
            Experience homestay living with the spaciousness of a private villa. Ideal for family holidays, group reunions, and peaceful couple stays in Madikeri.
          </p>
        </div>

        <div class="grid-2" style="align-items: center; gap: 3rem;">
          <div class="card-img-wrap" style="border-radius: var(--radius-lg); aspect-ratio: 16/10; box-shadow: var(--shadow-md);">
            <img src="assets/images/bedrooms/town-villa-coorg-master-bedroom-front.jpg" alt="Spacious 2-Bedroom Villa Master Bedroom">
          </div>
          <div>
            <span class="badge badge-gold" style="margin-bottom: 0.85rem;">Private 2-Bedroom Villa</span>
            <h3>Complete Private Villa Layout</h3>
            <p style="color: var(--color-text-muted); margin-top: 0.5rem; margin-bottom: 1.5rem;">
              Each of our four villas is thoughtfully designed as an independent accommodation unit featuring:
            </p>

            <ul style="list-style: none; display: flex; flex-direction: column; gap: 0.75rem; margin-bottom: 2rem;">
              <li style="display: flex; align-items: center; gap: 0.75rem;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--color-accent)" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                <span><strong>2 Private Bedrooms:</strong> Furnished with plush king and queen wooden beds.</span>
              </li>
              <li style="display: flex; align-items: center; gap: 0.75rem;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--color-accent)" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                <span><strong>Private Living Room:</strong> Comfortable sofa lounge with wall TV and room fan.</span>
              </li>
              <li style="display: flex; align-items: center; gap: 0.75rem;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--color-accent)" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                <span><strong>Dedicated Dining Area:</strong> Family table with chairs and full refrigerator.</span>
              </li>
              <li style="display: flex; align-items: center; gap: 0.75rem;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--color-accent)" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                <span><strong>Modern Attached Bathrooms:</strong> Clean tiles, western commodes & 24/7 hot geyser.</span>
              </li>
              <li style="display: flex; align-items: center; gap: 0.75rem;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--color-accent)" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                <span><strong>Guest Capacity:</strong> 6 to 8 guests per villa (1 extra bed per room on request).</span>
              </li>
            </ul>

            <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
              <a href="villas.html" class="btn btn-primary">View Villa Details & Floor Plan &rarr;</a>
              <a href="{WHATSAPP_PREFILLED}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp">Enquire on WhatsApp</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 04: AMENITIES & COMFORTS -->
    <section class="section" id="amenities">
      <div class="container">
        <div class="section-header">
          <span class="eyebrow">Thoughtful Facilities</span>
          <h2>Everything You Need for a Comfortable Stay</h2>
          <p class="section-subtitle">
            From round-the-clock hot water to dedicated power backup, we have equipped our Madikeri homestay with every practical amenity to ensure a hassle-free trip.
          </p>
        </div>

        {render_amenities_grid()}

        <div style="text-align: center; margin-top: 2.5rem;">
          <a href="amenities.html" class="btn btn-outline-dark">Explore All Verified Amenities &rarr;</a>
        </div>
      </div>
    </section>

    <!-- SECTION 05: A STAY FOR EVERY KIND OF TRAVELLER -->
    <section class="section" style="background-color: var(--color-surface);" id="stays">
      <div class="container">
        <div class="section-header">
          <span class="eyebrow">Tailored Experiences</span>
          <h2>A Stay for Every Kind of Traveller</h2>
          <p class="section-subtitle">
            Whether visiting Coorg as an intimate couple, with your children and grandparents, or organizing a large group reunion of up to 32 guests, our 4 private villas adapt seamlessly.
          </p>
        </div>

        <div class="grid-3">
          <!-- Card 1: Family Stays -->
          <div class="card">
            <div class="card-img-wrap">
              <span class="badge badge-gold card-badge">Family Favourite</span>
              <img src="assets/images/living-room/town-villa-coorg-living-room-wood.jpg" alt="Family Homestay in Madikeri Coorg">
            </div>
            <div class="card-body">
              <h3 class="card-title">Family Stays</h3>
              <p class="card-text">
                Enjoy having your entire family under one roof with 2 bedrooms, a private living hall for conversations, a dining area for kids' meals, and extra beds on request.
              </p>
              <a href="family-stay-madikeri.html" class="btn btn-outline-dark btn-sm" style="width: 100%;">
                Family Stay Details &rarr;
              </a>
            </div>
          </div>

          <!-- Card 2: Group Stays -->
          <div class="card">
            <div class="card-img-wrap">
              <span class="badge badge-gold card-badge">Up to 32 Guests</span>
              <img src="assets/images/villas/town-villa-coorg-suite-interior.jpg" alt="Group Accommodation in Madikeri Coorg">
            </div>
            <div class="card-body">
              <h3 class="card-title">Group Accommodation</h3>
              <p class="card-text">
                Travelling with friends, colleagues, or extended relatives? Book 2, 3, or all 4 villas to host groups of 12, 16, 24, up to 32 guests together with privacy and parking.
              </p>
              <a href="group-stay-madikeri.html" class="btn btn-outline-dark btn-sm" style="width: 100%;">
                Group Stay Details &rarr;
              </a>
            </div>
          </div>

          <!-- Card 3: Couple Stays -->
          <div class="card">
            <div class="card-img-wrap">
              <span class="badge badge-gold card-badge">Peaceful Retreat</span>
              <img src="assets/images/bedrooms/town-villa-coorg-second-bedroom-warm.jpg" alt="Couple Homestay in Madikeri Coorg">
            </div>
            <div class="card-body">
              <h3 class="card-title">Couple Getaways</h3>
              <p class="card-text">
                Relax in a tranquil private bedroom suite in central Madikeri, minutes from romantic sunset views at Raja's Seat and local Coorg coffee houses.
              </p>
              <a href="couple-stay-madikeri.html" class="btn btn-outline-dark btn-sm" style="width: 100%;">
                Couple Retreat Details &rarr;
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 06: MADIKERI ATTRACTIONS -->
    <section class="section" id="attractions">
      <div class="container">
        <div class="section-header">
          <span class="eyebrow">Local Sightseeing</span>
          <h2>Discover the Best of Madikeri, Coorg</h2>
          <p class="section-subtitle">
            Staying at Coorg Villa near Omkareshwara Temple means you are only minutes away from the town's most cherished historical landmarks and natural wonders.
          </p>
        </div>

        <div class="grid-4">
          <!-- Attraction 1: Omkareshwara Temple -->
          <div class="card">
            <div class="card-img-wrap">
              <span class="badge badge-gold card-badge">Next Door Landmark</span>
              <img src="assets/images/attractions/omkareshwara-temple.jpg" alt="Omkareshwara Temple Madikeri">
            </div>
            <div class="card-body">
              <h4 class="card-title">Omkareshwara Temple</h4>
              <p class="card-text">
                Famous 1820 historic Shiva shrine with unique Gothic and Islamic domes and sacred water pond with fish.
              </p>
              <a href="attractions/omkareshwara-temple.html" style="color: var(--color-accent); font-weight: 600; font-size: 0.9rem;">
                Read Visitor Guide &rarr;
              </a>
            </div>
          </div>

          <!-- Attraction 2: Raja's Seat -->
          <div class="card">
            <div class="card-img-wrap">
              <span class="badge badge-gold card-badge">Sunset Viewpoint</span>
              <img src="assets/images/attractions/rajas-seat.jpg" alt="Raja's Seat Sunset Garden Madikeri">
            </div>
            <div class="card-body">
              <h4 class="card-title">Raja's Seat</h4>
              <p class="card-text">
                Royal viewpoint overlooking rolling green valleys and mist-clad hills, ideal for golden sunset vistas.
              </p>
              <a href="attractions/rajas-seat.html" style="color: var(--color-accent); font-weight: 600; font-size: 0.9rem;">
                Read Visitor Guide &rarr;
              </a>
            </div>
          </div>

          <!-- Attraction 3: Madikeri Fort -->
          <div class="card">
            <div class="card-img-wrap">
              <span class="badge badge-gold card-badge">Historic Monument</span>
              <img src="assets/images/attractions/madikeri-fort.jpg" alt="Madikeri Fort and Palace">
            </div>
            <div class="card-body">
              <h4 class="card-title">Madikeri Fort</h4>
              <p class="card-text">
                17th-century heritage fortification featuring colonial architecture, palace, and archaeological museum.
              </p>
              <a href="attractions/madikeri-fort.html" style="color: var(--color-accent); font-weight: 600; font-size: 0.9rem;">
                Read Visitor Guide &rarr;
              </a>
            </div>
          </div>

          <!-- Attraction 4: Abbey Falls -->
          <div class="card">
            <div class="card-img-wrap">
              <span class="badge badge-gold card-badge">Scenic Waterfall</span>
              <img src="assets/images/attractions/abbey-falls.jpg" alt="Abbey Falls Madikeri Waterfall">
            </div>
            <div class="card-body">
              <h4 class="card-title">Abbey Falls</h4>
              <p class="card-text">
                Spectacular 70-foot waterfall cascading between private coffee estates and spice plantations.
              </p>
              <a href="attractions/abbey-falls.html" style="color: var(--color-accent); font-weight: 600; font-size: 0.9rem;">
                Read Visitor Guide &rarr;
              </a>
            </div>
          </div>
        </div>

        <div style="text-align: center; margin-top: 2.5rem;">
          <a href="places-to-visit-madikeri.html" class="btn btn-primary">View All Madikeri Sightseeing Places &rarr;</a>
        </div>
      </div>
    </section>

    <!-- SECTION 07: PROPERTY PHOTO GALLERY -->
    <section class="section" style="background-color: var(--color-surface);" id="gallery">
      <div class="container">
        <div class="section-header">
          <span class="eyebrow">Real Property Photographs</span>
          <h2>Take a Look Inside Coorg Villa</h2>
          <p class="section-subtitle">
            Explore authentic, unedited photos of our bedrooms, living areas, dining spaces, and facilities in Madikeri.
          </p>
        </div>

        <!-- Filter bar -->
        <div class="gallery-filter-bar">
          <button class="filter-btn active" data-filter="all">All Photos</button>
          <button class="filter-btn" data-filter="bedrooms">Bedrooms</button>
          <button class="filter-btn" data-filter="living">Living Rooms</button>
          <button class="filter-btn" data-filter="amenities">Dining & Amenities</button>
        </div>

        <!-- Gallery Grid (12 curated photos) -->
        <div class="gallery-grid">
          <div class="gallery-item" data-category="bedrooms" data-full="assets/images/bedrooms/town-villa-coorg-bedroom-spacious.jpg">
            <img src="assets/images/bedrooms/town-villa-coorg-bedroom-spacious.jpg" alt="Spacious Master Bedroom Suite" loading="lazy">
            <div class="gallery-item-overlay">
              <div class="gallery-caption">Master Bedroom with Lounge Seating & TV</div>
              <div class="gallery-category-tag">Bedroom</div>
            </div>
          </div>

          <div class="gallery-item" data-category="living" data-full="assets/images/villas/town-villa-coorg-living-dining-layout.jpg">
            <img src="assets/images/villas/town-villa-coorg-living-dining-layout.jpg" alt="Villa Living and Dining Open Layout" loading="lazy">
            <div class="gallery-item-overlay">
              <div class="gallery-caption">Living Room, Refrigerator & Dining Area</div>
              <div class="gallery-category-tag">Villa Layout</div>
            </div>
          </div>

          <div class="gallery-item" data-category="bedrooms" data-full="assets/images/bedrooms/town-villa-coorg-master-bedroom-front.jpg">
            <img src="assets/images/bedrooms/town-villa-coorg-master-bedroom-front.jpg" alt="Master Bedroom King Bed" loading="lazy">
            <div class="gallery-item-overlay">
              <div class="gallery-caption">Solid Wood Bed & Fresh Linens</div>
              <div class="gallery-category-tag">Bedroom</div>
            </div>
          </div>

          <div class="gallery-item" data-category="living" data-full="assets/images/living-room/town-villa-coorg-living-room-sofas.jpg">
            <img src="assets/images/living-room/town-villa-coorg-living-room-sofas.jpg" alt="Private Living Hall with Sofa Seating" loading="lazy">
            <div class="gallery-item-overlay">
              <div class="gallery-caption">Private Living Room with Wall TV</div>
              <div class="gallery-category-tag">Living Room</div>
            </div>
          </div>

          <div class="gallery-item" data-category="bedrooms" data-full="assets/images/bedrooms/town-villa-coorg-second-bedroom-warm.jpg">
            <img src="assets/images/bedrooms/town-villa-coorg-second-bedroom-warm.jpg" alt="Second Bedroom Warm Ambient Light" loading="lazy">
            <div class="gallery-item-overlay">
              <div class="gallery-caption">Second Bedroom with Nightstand & Fan</div>
              <div class="gallery-category-tag">Bedroom</div>
            </div>
          </div>

          <div class="gallery-item" data-category="amenities" data-full="assets/images/amenities/town-villa-coorg-dining-refrigerator.jpg">
            <img src="assets/images/amenities/town-villa-coorg-dining-refrigerator.jpg" alt="Dining Table and Refrigerator" loading="lazy">
            <div class="gallery-item-overlay">
              <div class="gallery-caption">Family Dining Space with In-Villa Refrigerator</div>
              <div class="gallery-category-tag">Amenities</div>
            </div>
          </div>

          <div class="gallery-item" data-category="amenities" data-full="assets/images/amenities/town-villa-coorg-attached-bathroom.jpg">
            <img src="assets/images/amenities/town-villa-coorg-attached-bathroom.jpg" alt="Attached Modern Bathroom with Hot Geyser" loading="lazy">
            <div class="gallery-item-overlay">
              <div class="gallery-caption">Attached Bathroom with 24/7 Hot Water Geyser</div>
              <div class="gallery-category-tag">Bathroom</div>
            </div>
          </div>

          <div class="gallery-item" data-category="living" data-full="assets/images/living-room/town-villa-coorg-living-room-wood.jpg">
            <img src="assets/images/living-room/town-villa-coorg-living-room-wood.jpg" alt="Living Room with Power Backup Inverter" loading="lazy">
            <div class="gallery-item-overlay">
              <div class="gallery-caption">Living Hall with Dedicated Power Backup Inverter</div>
              <div class="gallery-category-tag">Living Room</div>
            </div>
          </div>
        </div>

        <div style="text-align: center; margin-top: 2.5rem;">
          <a href="gallery.html" class="btn btn-outline-dark">View Full Photo Gallery (24+ Photos) &rarr;</a>
        </div>
      </div>
    </section>

    <!-- SECTION 08: LOCATION ADVANTAGE & MAP -->
    <section class="section" id="location">
      <div class="container">
        <div class="grid-2" style="align-items: center; gap: 3rem;">
          <div>
            <span class="eyebrow">Prime Central Location</span>
            <h2>Stay Near Omkareshwara Temple in Madikeri</h2>
            <p style="margin-top: 1rem;">
              Location is everything when choosing accommodation in Coorg. Staying on the remote outskirts can mean spending hours navigating winding hill roads after dark. Coorg Villa is situated conveniently near Omkareshwara Temple in central Madikeri.
            </p>
            <p>
              You enjoy instant walking and driving access to the town's vibrant restaurants, authentic Kodava spice shops, coffee stores, and heritage viewpoints, all while relaxing in a quiet, residential villa enclave.
            </p>
            <div style="margin-top: 1.5rem; display: flex; flex-direction: column; gap: 0.65rem;">
              <div style="display: flex; gap: 0.75rem;">
                <strong style="color: var(--color-primary); min-width: 140px;">Landmark:</strong>
                <span style="color: var(--color-text-muted);">Near Omkareshwara Temple, Madikeri</span>
              </div>
              <div style="display: flex; gap: 0.75rem;">
                <strong style="color: var(--color-primary); min-width: 140px;">Madikeri Fort:</strong>
                <span style="color: var(--color-text-muted);">~1.2 km (4 minutes drive)</span>
              </div>
              <div style="display: flex; gap: 0.75rem;">
                <strong style="color: var(--color-primary); min-width: 140px;">Raja's Seat:</strong>
                <span style="color: var(--color-text-muted);">~1.8 km (6 minutes drive)</span>
              </div>
              <div style="display: flex; gap: 0.75rem;">
                <strong style="color: var(--color-primary); min-width: 140px;">Abbey Falls:</strong>
                <span style="color: var(--color-text-muted);">~8.5 km (20 minutes scenic drive)</span>
              </div>
            </div>
            <div style="margin-top: 2rem;">
              <a href="location.html" class="btn btn-primary">Location Guide & Driving Routes &rarr;</a>
            </div>
          </div>

          <div>
            <div style="border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-md); border: 1px solid var(--color-border); background: var(--color-surface); padding: 0.75rem;">
              <iframe
                title="Madikeri, Coorg location map"
                src="https://www.google.com/maps?q=Madikeri%2C%20Karnataka&output=embed"
                width="100%"
                height="380"
                style="border:0;border-radius:12px; display:block;"
                loading="lazy"
                referrerpolicy="no-referrer-when-downgrade"
                allowfullscreen>
              </iframe>
              <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.75rem 0.5rem 0.25rem 0.5rem;">
                <span style="font-size: 0.85rem; color: var(--color-text-muted);">Madikeri Town Location (Near Omkareshwara Temple)</span>
                <a href="https://maps.google.com/?q=Madikeri+Karnataka" target="_blank" rel="noopener noreferrer" style="font-size: 0.85rem; font-weight: 600; color: var(--color-accent);">Open in Maps &rarr;</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 10: FREQUENTLY ASKED QUESTIONS -->
    <section class="section" style="background-color: var(--color-surface);" id="faq">
      <div class="container">
        <div class="section-header">
          <span class="eyebrow">Got Questions?</span>
          <h2>Frequently Asked Questions</h2>
          <p class="section-subtitle">
            Find quick answers regarding our villas, capacities, parking, hot water, and booking procedures.
          </p>
        </div>

        {render_faq_accordions()}

        <div style="text-align: center; margin-top: 2.5rem;">
          <a href="faq.html" class="btn btn-outline-dark">Read All FAQs &rarr;</a>
        </div>
      </div>
    </section>

    <!-- SECTION 11: FINAL BOOKING CTA & ENQUIRY ENGINE -->
    <section class="section" id="booking">
      <div class="container">
        <div class="section-header">
          <span class="eyebrow">Plan Your Stay in Coorg</span>
          <h2>Planning Your Stay in Madikeri?</h2>
          <p class="section-subtitle">
            Check availability for your preferred dates and contact Coorg Villa directly for instant confirmation and the best tariff.
          </p>
        </div>

        {render_booking_form()}
      </div>
    </section>

    {render_lightbox_modal()}
    """
    return render_page(
        title="Homestay in Madikeri, Coorg | Coorg Villa",
        description="Book a comfortable stay at Coorg Villa in Madikeri. Explore our 2-bedroom villas for families, groups and couples near Omkareshwara Temple.",
        canonical_slug="",
        body_content=body,
        active_tab="HOME",
        root_path="",
        schema_json=base_business_schema
    )

def build_villas_page():
    body = f"""
    <div style="background-color: var(--color-primary-dark); color: #FFFFFF; padding: 4rem 0 3rem 0; text-align: center;">
      <div class="container">
        <span class="eyebrow" style="color: var(--color-accent-light);">Homestay Accommodation</span>
        <h1 style="color: #FFFFFF; margin-top: 0.5rem;">2-Bedroom Villas in Madikeri, Coorg</h1>
        <p style="max-width: 680px; margin: 1rem auto 0 auto; color: rgba(255,255,255,0.85); font-size: 1.1rem;">
          Spacious 2-bedroom private villas equipped with private living room, dining space, modern attached bathrooms, high-speed Wi-Fi, and power backup.
        </p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="grid-2" style="align-items: center; gap: 3.5rem; margin-bottom: 4rem;">
          <div class="card-img-wrap" style="border-radius: var(--radius-lg); aspect-ratio: 4/3; box-shadow: var(--shadow-lg);">
            <img src="assets/images/villas/town-villa-coorg-bedroom-suite.jpg" alt="Master Bedroom in Coorg Villa">
          </div>
          <div>
            <span class="badge badge-gold" style="margin-bottom: 0.75rem;">Independent Villa Unit</span>
            <h2>Spacious 2-Bedroom Layout (4 Villas Available)</h2>
            <p style="margin-top: 1rem;">
              Coorg Villa features four independent 2-bedroom villas. Each villa is a complete, self-contained home designed to offer comfort and togetherness for families, friends, and couples travelling to Kodagu.
            </p>
            <p>
              Unlike conventional hotels where groups are split across isolated hotel rooms, our villas allow everyone to gather comfortably in a private living hall and share meals at the dining table while retaining the privacy of separate bedrooms.
            </p>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1.5rem; margin-bottom: 2rem;">
              <div style="background: var(--color-surface); padding: 1rem; border-radius: var(--radius-md); border: 1px solid var(--color-border);">
                <strong style="color: var(--color-primary); font-size: 1.25rem; display: block;">2 Bedrooms</strong>
                <span style="font-size: 0.85rem; color: var(--color-text-muted);">King & Queen beds with wooden finish</span>
              </div>
              <div style="background: var(--color-surface); padding: 1rem; border-radius: var(--radius-md); border: 1px solid var(--color-border);">
                <strong style="color: var(--color-primary); font-size: 1.25rem; display: block;">6–8 Guests</strong>
                <span style="font-size: 0.85rem; color: var(--color-text-muted);">Per villa (up to 32 guests across all 4)</span>
              </div>
              <div style="background: var(--color-surface); padding: 1rem; border-radius: var(--radius-md); border: 1px solid var(--color-border);">
                <strong style="color: var(--color-primary); font-size: 1.25rem; display: block;">Living Hall</strong>
                <span style="font-size: 0.85rem; color: var(--color-text-muted);">Sofa lounge with LED TV & Fan</span>
              </div>
              <div style="background: var(--color-surface); padding: 1rem; border-radius: var(--radius-md); border: 1px solid var(--color-border);">
                <strong style="color: var(--color-primary); font-size: 1.25rem; display: block;">Dining Area</strong>
                <span style="font-size: 0.85rem; color: var(--color-text-muted);">With full-size refrigerator</span>
              </div>
            </div>
            <a href="#booking-enquiry" class="btn btn-primary">Enquire About Villa Availability &rarr;</a>
          </div>
        </div>

        <!-- Room Features Breakdown -->
        <div class="section-header">
          <span class="eyebrow">Room By Room</span>
          <h2>Inside Each 2-Bedroom Villa</h2>
          <p class="section-subtitle">
            Explore the layout and components that make Coorg Villa one of the most practical accommodation choices in Madikeri.
          </p>
        </div>

        <div class="grid-3">
          <div class="card">
            <div class="card-img-wrap">
              <img src="assets/images/bedrooms/town-villa-coorg-master-bedroom-front.jpg" alt="Master Bedroom">
            </div>
            <div class="card-body">
              <h3 class="card-title">1. Master Bedroom</h3>
              <p class="card-text">
                Spacious room featuring solid wood paneled ceiling, king-sized bed, comfortable lounge chairs, wooden wardrobe with dressing mirror, and wall-mounted TV.
              </p>
              <ul style="font-size: 0.85rem; color: var(--color-text-muted); list-style: disc; margin-left: 1.2rem; line-height: 1.6;">
                <li>King-size bed with crisp linens</li>
                <li>Lounge armchairs & coffee table</li>
                <li>Attached modern bathroom</li>
                <li>Space for 1 extra bed</li>
              </ul>
            </div>
          </div>

          <div class="card">
            <div class="card-img-wrap">
              <img src="assets/images/bedrooms/town-villa-coorg-second-bedroom-warm.jpg" alt="Second Cozy Bedroom">
            </div>
            <div class="card-body">
              <h3 class="card-title">2. Second Bedroom</h3>
              <p class="card-text">
                Warm and peaceful bedroom fitted with comfortable double/queen bed, bedside nightstand, wall fan, privacy curtains, and calming mood lighting.
              </p>
              <ul style="font-size: 0.85rem; color: var(--color-text-muted); list-style: disc; margin-left: 1.2rem; line-height: 1.6;">
                <li>Comfortable queen wooden bed</li>
                <li>Bedside lamp & nightstand</li>
                <li>Quiet ambience for restful sleep</li>
                <li>Extra mattress available</li>
              </ul>
            </div>
          </div>

          <div class="card">
            <div class="card-img-wrap">
              <img src="assets/images/living-room/town-villa-coorg-living-room-sofas.jpg" alt="Private Living Room">
            </div>
            <div class="card-body">
              <h3 class="card-title">3. Living & Dining Hall</h3>
              <p class="card-text">
                Private living space featuring 3-seater and single armchairs, tea table, LED TV, inverter power backup, and dining table with full refrigerator.
              </p>
              <ul style="font-size: 0.85rem; color: var(--color-text-muted); list-style: disc; margin-left: 1.2rem; line-height: 1.6;">
                <li>Plush sofa seating for the group</li>
                <li>Family dining table</li>
                <li>Refrigerator for drinks & snacks</li>
                <li>Dedicated power backup unit</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Booking Component Anchor -->
        <div style="margin-top: 5rem;">
          {render_booking_form()}
        </div>
      </div>
    </section>
    """
    return render_page(
        title="2-Bedroom Villas in Madikeri, Coorg | Coorg Villa",
        description="Discover spacious 2-bedroom villas in Madikeri with Wi-Fi, living and dining areas, hot water and parking. Enquire about your stay.",
        canonical_slug="villas.html",
        body_content=body,
        active_tab="VILLAS",
        root_path=""
    )

def build_amenities_page():
    body = f"""
    <div style="background-color: var(--color-primary-dark); color: #FFFFFF; padding: 4rem 0 3rem 0; text-align: center;">
      <div class="container">
        <span class="eyebrow" style="color: var(--color-accent-light);">Homestay Facilities</span>
        <h1 style="color: #FFFFFF; margin-top: 0.5rem;">Facilities at Coorg Villa</h1>
        <p style="max-width: 680px; margin: 1rem auto 0 auto; color: rgba(255,255,255,0.85); font-size: 1.1rem;">
          Detailed descriptions of the verified amenities and comforts provided across all 4 of our Madikeri villas.
        </p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="section-header">
          <span class="eyebrow">Verified & Maintained</span>
          <h2>All Amenities at a Glance</h2>
          <p class="section-subtitle">
            Every villa is maintained to the highest hygiene and hospitality standards, ensuring your family or group enjoys complete peace of mind.
          </p>
        </div>

        {render_amenities_grid()}

        <!-- Feature Highlight Row -->
        <div class="grid-2" style="align-items: center; gap: 3.5rem; margin-top: 5rem;">
          <div>
            <span class="eyebrow">Round-the-Clock Comfort</span>
            <h3>Continuous Hot Water & Inverter Backup</h3>
            <p style="margin-top: 1rem;">
              Madikeri's cool mornings and mountain weather call for reliable amenities. We have equipped our property with dedicated water geysers ensuring instant hot water for baths at any hour of the day.
            </p>
            <p>
              Each villa also includes an inverter power backup system so that lights, fans, and mobile charging remain completely operational regardless of weather or regional grid fluctuations.
            </p>
            <div style="margin-top: 1.5rem;">
              <a href="contact.html" class="btn btn-primary">Book Your Stay &rarr;</a>
            </div>
          </div>
          <div class="card-img-wrap" style="border-radius: var(--radius-lg); aspect-ratio: 4/3; box-shadow: var(--shadow-md);">
            <img src="assets/images/amenities/town-villa-coorg-attached-bathroom.jpg" alt="Attached Bathroom with Geyser">
          </div>
        </div>

        <div style="margin-top: 5rem;">
          {render_booking_form()}
        </div>
      </div>
    </section>
    """
    return render_page(
        title="Facilities at Coorg Villa | Madikeri Homestay Amenities",
        description="Explore the verified amenities at Coorg Villa including 2 bedrooms per villa, private living hall, Wi-Fi, refrigerator, power backup, and hot water.",
        canonical_slug="amenities.html",
        body_content=body,
        active_tab="AMENITIES",
        root_path=""
    )

def build_gallery_page():
    # 24 real curated photos
    gallery_photos = [
        ("town-villa-coorg-bedroom-spacious.jpg", "bedrooms", "Spacious Master Bedroom Suite with TV & Wardrobe"),
        ("town-villa-coorg-living-dining-layout.jpg", "living", "Villa Open Layout: Living Room, Refrigerator & Dining"),
        ("town-villa-coorg-master-bedroom-front.jpg", "bedrooms", "Master Bedroom King Bed with Wooden Frame"),
        ("town-villa-coorg-living-room-sofas.jpg", "living", "Private Living Room with Sofa Set & Wall TV"),
        ("town-villa-coorg-master-bedroom-angle.jpg", "bedrooms", "Master Bedroom Angle View with White Linens"),
        ("town-villa-coorg-second-bedroom-warm.jpg", "bedrooms", "Second Bedroom with Warm Ambient Light & Nightstand"),
        ("town-villa-coorg-dining-refrigerator.jpg", "amenities", "Family Dining Table with Refrigerator"),
        ("town-villa-coorg-living-room-wood.jpg", "living", "Living Room with Solid Wood Furniture & Inverter Backup"),
        ("town-villa-coorg-attached-bathroom.jpg", "amenities", "Attached Bathroom with Hot Water Geyser & Shower"),
        ("town-villa-coorg-bedroom-balcony.jpg", "bedrooms", "Master Bedroom with Balcony Access"),
        ("town-villa-coorg-bedroom-lounge.jpg", "bedrooms", "Master Bedroom Lounge Armchairs & Wood Ceiling"),
        ("town-villa-coorg-living-room-brown.jpg", "living", "Living Room with Chocolate Plush Sofas"),
        ("town-villa-coorg-bedroom-deluxe.jpg", "bedrooms", "Deluxe Bedroom with White Bedding & Maroon Runners"),
        ("town-villa-coorg-second-bedroom-night.jpg", "bedrooms", "Second Bedroom Night Ambience"),
        ("town-villa-coorg-living-room-bright.jpg", "living", "Living Room Bright Natural Lighting"),
        ("town-villa-coorg-entrance-hallway.jpg", "amenities", "Entrance Hallway with Red Carpet Runner & Downlights"),
        ("town-villa-coorg-stairs-landing.jpg", "amenities", "Staircase Landing Leading to Upper Villas"),
        ("town-villa-coorg-suite-interior.jpg", "living", "Villa Suite Open View Looking Towards Bedrooms"),
        ("town-villa-coorg-second-bedroom-cozy.jpg", "bedrooms", "Second Bedroom Vertical View with Nightstand"),
        ("town-villa-coorg-second-bedroom-ambient.jpg", "bedrooms", "Second Bedroom Ambient Violet Night Glow"),
        ("town-villa-coorg-second-bedroom-blue.jpg", "bedrooms", "Second Bedroom Blue Evening Lighting"),
        ("town-villa-coorg-living-room-evening.jpg", "living", "Living Room Evening Lighting with TV"),
        ("town-villa-coorg-fresh-linen.jpg", "amenities", "Fresh White Towels & Sanitized Linens"),
        ("town-villa-coorg-living-room-blue-mood.jpg", "living", "Living Room Cove Lighting Effect")
    ]

    items_html = ""
    for fname, cat, cap in gallery_photos:
        items_html += f"""
        <div class="gallery-item" data-category="{cat}" data-full="assets/images/gallery/{fname}">
          <img src="assets/images/gallery/{fname}" alt="{cap}" loading="lazy">
          <div class="gallery-item-overlay">
            <div class="gallery-caption">{cap}</div>
            <div class="gallery-category-tag">{cat.capitalize()}</div>
          </div>
        </div>
        """

    body = f"""
    <div style="background-color: var(--color-primary-dark); color: #FFFFFF; padding: 4rem 0 3rem 0; text-align: center;">
      <div class="container">
        <span class="eyebrow" style="color: var(--color-accent-light);">Authentic Visuals</span>
        <h1 style="color: #FFFFFF; margin-top: 0.5rem;">Photos of Coorg Villa</h1>
        <p style="max-width: 680px; margin: 1rem auto 0 auto; color: rgba(255,255,255,0.85); font-size: 1.1rem;">
          Explore real, unedited photographs of our 2-bedroom villas, living areas, dining spaces, and facilities in Madikeri.
        </p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <!-- Filter bar -->
        <div class="gallery-filter-bar">
          <button class="filter-btn active" data-filter="all">All Photos (24)</button>
          <button class="filter-btn" data-filter="bedrooms">Bedrooms</button>
          <button class="filter-btn" data-filter="living">Living Rooms</button>
          <button class="filter-btn" data-filter="amenities">Dining & Property</button>
        </div>

        <div class="gallery-grid">
          {items_html}
        </div>

        <div style="margin-top: 5rem;">
          {render_booking_form()}
        </div>
      </div>
    </section>

    {render_lightbox_modal()}
    """
    return render_page(
        title="Coorg Villa Photos | Madikeri Homestay Gallery",
        description="Explore photos of Coorg Villa, including bedrooms, living areas and facilities at our Madikeri homestay.",
        canonical_slug="gallery.html",
        body_content=body,
        active_tab="GALLERY",
        root_path=""
    )

def build_family_stay_page():
    body = f"""
    <div style="background-color: var(--color-primary-dark); color: #FFFFFF; padding: 4rem 0 3rem 0; text-align: center;">
      <div class="container">
        <span class="eyebrow" style="color: var(--color-accent-light);">Family Vacations in Coorg</span>
        <h1 style="color: #FFFFFF; margin-top: 0.5rem;">Family Homestay in Madikeri, Coorg</h1>
        <p style="max-width: 680px; margin: 1rem auto 0 auto; color: rgba(255,255,255,0.85); font-size: 1.1rem;">
          Spacious 2-bedroom villas offering privacy, comfortable living spaces, and home-like convenience for families with children and elderly parents.
        </p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="grid-2" style="align-items: center; gap: 3.5rem; margin-bottom: 4rem;">
          <div>
            <span class="eyebrow">Family Comfort</span>
            <h2>Why Families Choose Coorg Villa</h2>
            <p style="margin-top: 1rem;">
              Travelling with family—especially with toddlers, children, or elderly parents—requires much more than just a place to sleep. Staying in isolated hotel rooms often means having to call across rooms, having no common space to relax together, and eating food awkwardly on bed edges.
            </p>
            <p>
              At Coorg Villa, each of our four 2-bedroom villas provides the comfort and functionality of a private vacation home:
            </p>
            <ul style="list-style: none; display: flex; flex-direction: column; gap: 0.75rem; margin: 1.5rem 0;">
              <li style="display: flex; gap: 0.75rem;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--color-accent)" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                <span><strong>Stay Together in One Unit:</strong> 2 private bedrooms allow parents, children, or grandparents to enjoy personal privacy while sharing the same front door.</span>
              </li>
              <li style="display: flex; gap: 0.75rem;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--color-accent)" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                <span><strong>Private Living Room:</strong> Ample sofa seating where the entire family can unwind, plan the next day's itinerary, and watch television together.</span>
              </li>
              <li style="display: flex; gap: 0.75rem;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--color-accent)" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                <span><strong>Dining Table & In-Villa Fridge:</strong> Store milk, baby food, fruits, medicines, and snacks comfortably in the refrigerator, and enjoy family meals together.</span>
              </li>
              <li style="display: flex; gap: 0.75rem;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--color-accent)" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                <span><strong>Extra Bedding:</strong> Additional beds are easily arranged (1 per bedroom) so families of up to 8 members stay comfortably.</span>
              </li>
            </ul>
            <a href="#booking-enquiry" class="btn btn-primary">Make a Family Booking Enquiry &rarr;</a>
          </div>
          <div class="card-img-wrap" style="border-radius: var(--radius-lg); aspect-ratio: 4/3; box-shadow: var(--shadow-lg);">
            <img src="assets/images/living-room/town-villa-coorg-living-room-wood.jpg" alt="Family Sitting Area in Coorg Villa">
          </div>
        </div>

        <div style="margin-top: 5rem;">
          {render_booking_form()}
        </div>
      </div>
    </section>
    """
    return render_page(
        title="Family Homestay in Madikeri, Coorg | Coorg Villa",
        description="Plan a family stay in Madikeri with spacious 2-bedroom villa accommodation for 6–8 guests per villa. Contact us to check availability.",
        canonical_slug="family-stay-madikeri.html",
        body_content=body,
        active_tab="FAMILY",
        root_path=""
    )

def build_group_stay_page():
    body = f"""
    <div style="background-color: var(--color-primary-dark); color: #FFFFFF; padding: 4rem 0 3rem 0; text-align: center;">
      <div class="container">
        <span class="eyebrow" style="color: var(--color-accent-light);">Group Stays in Coorg</span>
        <h1 style="color: #FFFFFF; margin-top: 0.5rem;">Group Accommodation in Madikeri, Coorg</h1>
        <p style="max-width: 680px; margin: 1rem auto 0 auto; color: rgba(255,255,255,0.85); font-size: 1.1rem;">
          Hosting 12, 16, 24, up to 32 guests across 4 spacious 2-bedroom villas in central Madikeri with on-site parking and shared living halls.
        </p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="grid-2" style="align-items: center; gap: 3.5rem; margin-bottom: 4rem;">
          <div>
            <span class="eyebrow">Capacity Up to 32 Guests</span>
            <h2>Book Multiple Villas for Group Getaways</h2>
            <p style="margin-top: 1rem;">
              Organizing accommodation for college friends reunions, extended family gatherings, trekking clubs, or corporate team offsites in Coorg can be tricky. Standard hotels scatter group members across different floors, while isolated cottages often lack vehicle parking and town access.
            </p>
            <p>
              Coorg Villa solves this with an ideal architectural setup:
            </p>
            <div style="display: flex; flex-direction: column; gap: 1rem; margin: 1.5rem 0;">
              <div style="background: var(--color-surface); padding: 1.25rem; border-radius: var(--radius-md); border-left: 4px solid var(--color-accent); border: 1px solid var(--color-border);">
                <strong style="color: var(--color-primary); font-size: 1.1rem; display: block;">1 Villa: 6–8 Guests</strong>
                <span style="font-size: 0.9rem; color: var(--color-text-muted);">2 Bedrooms, 1 Living Hall, 1 Dining Space, Attached Baths</span>
              </div>
              <div style="background: var(--color-surface); padding: 1.25rem; border-radius: var(--radius-md); border-left: 4px solid var(--color-accent); border: 1px solid var(--color-border);">
                <strong style="color: var(--color-primary); font-size: 1.1rem; display: block;">2 Villas: 12–16 Guests</strong>
                <span style="font-size: 0.9rem; color: var(--color-text-muted);">4 Bedrooms, 2 Living Rooms, 2 Dining Areas, 4 Bathrooms</span>
              </div>
              <div style="background: var(--color-surface); padding: 1.25rem; border-radius: var(--radius-md); border-left: 4px solid var(--color-accent); border: 1px solid var(--color-border);">
                <strong style="color: var(--color-primary); font-size: 1.1rem; display: block;">Full Property (4 Villas): 24–32 Guests</strong>
                <span style="font-size: 0.9rem; color: var(--color-text-muted);">All 8 Bedrooms, 4 Living Halls, exclusive property access with parking for traveller tempo vans & cars.</span>
              </div>
            </div>
            <a href="#booking-enquiry" class="btn btn-primary">Request Group Booking Tariff &rarr;</a>
          </div>
          <div class="card-img-wrap" style="border-radius: var(--radius-lg); aspect-ratio: 4/3; box-shadow: var(--shadow-lg);">
            <img src="assets/images/villas/town-villa-coorg-living-dining-layout.jpg" alt="Group Accommodation Layout in Madikeri">
          </div>
        </div>

        <div style="margin-top: 5rem;">
          {render_booking_form()}
        </div>
      </div>
    </section>
    """
    return render_page(
        title="Group Accommodation in Madikeri, Coorg | Coorg Villa (Up to 32)",
        description="Book group stays in Madikeri, Coorg for 12, 16, 24 up to 32 guests across 4 spacious 2-bedroom villas with private living halls and on-site parking.",
        canonical_slug="group-stay-madikeri.html",
        body_content=body,
        active_tab="GROUP",
        root_path=""
    )

def build_couple_stay_page():
    body = f"""
    <div style="background-color: var(--color-primary-dark); color: #FFFFFF; padding: 4rem 0 3rem 0; text-align: center;">
      <div class="container">
        <span class="eyebrow" style="color: var(--color-accent-light);">Romantic & Peaceful Coorg</span>
        <h1 style="color: #FFFFFF; margin-top: 0.5rem;">Comfortable Homestay for Couples in Madikeri</h1>
        <p style="max-width: 680px; margin: 1rem auto 0 auto; color: rgba(255,255,255,0.85); font-size: 1.1rem;">
          Enjoy privacy, boutique hospitality, and walking access to Madikeri's cozy cafes and Raja's Seat sunset garden.
        </p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="grid-2" style="align-items: center; gap: 3.5rem; margin-bottom: 4rem;">
          <div>
            <span class="eyebrow">Tranquil Atmosphere</span>
            <h2>Serene & Private Couple Retreat</h2>
            <p style="margin-top: 1rem;">
              Coorg is renowned as the "Scotland of India" for its romantic misty mountains, pleasant cool climate, and picturesque coffee plantations. If you are planning a weekend couple getaway or anniversary retreat, Coorg Villa offers a tranquil boutique sanctuary right in town.
            </p>
            <p>
              Wake up to cool hill breezes, sip fresh Kodagu filter coffee, take a gentle morning walk around Omkareshwara Temple's tranquil waters, and catch magical golden hour sunsets at Raja's Seat just 5 minutes away.
            </p>
            <ul style="list-style: none; display: flex; flex-direction: column; gap: 0.75rem; margin: 1.5rem 0;">
              <li style="display: flex; gap: 0.75rem;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--color-accent)" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                <span><strong>Peaceful, Private Bedroom Suite:</strong> King wooden bed, cozy lounge chairs, and ambient mood lighting.</span>
              </li>
              <li style="display: flex; gap: 0.75rem;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--color-accent)" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                <span><strong>Walk to Top Madikeri Cafes:</strong> Enjoy central access without spending half your holiday driving.</span>
              </li>
              <li style="display: flex; gap: 0.75rem;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--color-accent)" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                <span><strong>Instant Hot Water:</strong> Relax in soothing hot showers after evening walks in cool weather.</span>
              </li>
            </ul>
            <a href="#booking-enquiry" class="btn btn-primary">Enquire for Two Guests &rarr;</a>
          </div>
          <div class="card-img-wrap" style="border-radius: var(--radius-lg); aspect-ratio: 4/3; box-shadow: var(--shadow-lg);">
            <img src="assets/images/bedrooms/town-villa-coorg-second-bedroom-warm.jpg" alt="Cozy Bedroom Suite for Couples">
          </div>
        </div>

        <div style="margin-top: 5rem;">
          {render_booking_form()}
        </div>
      </div>
    </section>
    """
    return render_page(
        title="Comfortable Homestay for Couples in Madikeri | Coorg Villa",
        description="Looking for a peaceful couple stay in Madikeri, Coorg? Enjoy private villa accommodation with Wi-Fi, hot water, and easy access to Raja's Seat sunset viewpoint.",
        canonical_slug="couple-stay-madikeri.html",
        body_content=body,
        active_tab="COUPLE",
        root_path=""
    )

def build_places_page():
    body = f"""
    <div style="background-color: var(--color-primary-dark); color: #FFFFFF; padding: 4rem 0 3rem 0; text-align: center;">
      <div class="container">
        <span class="eyebrow" style="color: var(--color-accent-light);">Madikeri Sightseeing Guide</span>
        <h1 style="color: #FFFFFF; margin-top: 0.5rem;">Places to Visit Near Coorg Villa</h1>
        <p style="max-width: 680px; margin: 1rem auto 0 auto; color: rgba(255,255,255,0.85); font-size: 1.1rem;">
          Explore the top tourist attractions, historical landmarks, waterfalls, and viewpoints easily accessible from our central homestay.
        </p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="section-header">
          <span class="eyebrow">Local Attractions</span>
          <h2>Madikeri's Must-Visit Destinations</h2>
          <p class="section-subtitle">
            Staying in central Madikeri near Omkareshwara Temple gives you a tremendous advantage: you save travel time and can visit key attractions during early morning and golden sunset hours.
          </p>
        </div>

        <div class="grid-3" style="gap: 2.5rem;">
          <!-- 1. Omkareshwara Temple -->
          <div class="card">
            <div class="card-img-wrap">
              <span class="badge badge-gold card-badge">Next Door Landmark</span>
              <img src="assets/images/attractions/omkareshwara-temple.jpg" alt="Omkareshwara Temple Madikeri">
            </div>
            <div class="card-body">
              <h3 class="card-title">Omkareshwara Temple</h3>
              <p class="card-text">
                Built in 1820 by King Lingarajendra II, this historic Shiva temple is famous for its unique Gothic and Islamic dome architecture and sacred water pond with fish.
              </p>
              <div style="margin-bottom: 1.25rem; font-size: 0.85rem; color: var(--color-accent); font-weight: 600;">
                Distance: Walking distance from villa
              </div>
              <a href="attractions/omkareshwara-temple.html" class="btn btn-outline-dark btn-sm" style="width: 100%;">Read Full Visitor Guide &rarr;</a>
            </div>
          </div>

          <!-- 2. Raja's Seat -->
          <div class="card">
            <div class="card-img-wrap">
              <span class="badge badge-gold card-badge">Sunset Garden</span>
              <img src="assets/images/attractions/rajas-seat.jpg" alt="Raja's Seat Viewpoint Madikeri">
            </div>
            <div class="card-body">
              <h3 class="card-title">Raja's Seat</h3>
              <p class="card-text">
                The royal viewing pavilion surrounded by seasonal flowers and musical fountains. Offers dramatic sunset views over the misty mountains of Kodagu.
              </p>
              <div style="margin-bottom: 1.25rem; font-size: 0.85rem; color: var(--color-accent); font-weight: 600;">
                Distance: ~1.8 km (6 mins drive)
              </div>
              <a href="attractions/rajas-seat.html" class="btn btn-outline-dark btn-sm" style="width: 100%;">Read Full Visitor Guide &rarr;</a>
            </div>
          </div>

          <!-- 3. Madikeri Fort -->
          <div class="card">
            <div class="card-img-wrap">
              <span class="badge badge-gold card-badge">17th-Century Fort</span>
              <img src="assets/images/attractions/madikeri-fort.jpg" alt="Madikeri Fort and Palace">
            </div>
            <div class="card-body">
              <h3 class="card-title">Madikeri Fort</h3>
              <p class="card-text">
                Originally built by Mudduraja and later rebuilt in stone by Tipu Sultan. Houses an archaeological museum, church, and panoramic views of the town.
              </p>
              <div style="margin-bottom: 1.25rem; font-size: 0.85rem; color: var(--color-accent); font-weight: 600;">
                Distance: ~1.2 km (4 mins drive)
              </div>
              <a href="attractions/madikeri-fort.html" class="btn btn-outline-dark btn-sm" style="width: 100%;">Read Full Visitor Guide &rarr;</a>
            </div>
          </div>

          <!-- 4. Abbey Falls -->
          <div class="card">
            <div class="card-img-wrap">
              <span class="badge badge-gold card-badge">Scenic Waterfall</span>
              <img src="assets/images/attractions/abbey-falls.jpg" alt="Abbey Falls Madikeri">
            </div>
            <div class="card-body">
              <h3 class="card-title">Abbey Falls</h3>
              <p class="card-text">
                A 70-foot waterfall cascading between private coffee estates and spice plantations. A hanging bridge offers breathtaking views of the waterfall.
              </p>
              <div style="margin-bottom: 1.25rem; font-size: 0.85rem; color: var(--color-accent); font-weight: 600;">
                Distance: ~8.5 km (20 mins drive)
              </div>
              <a href="attractions/abbey-falls.html" class="btn btn-outline-dark btn-sm" style="width: 100%;">Read Full Visitor Guide &rarr;</a>
            </div>
          </div>

          <!-- 5. Raja's Tomb (Gaddige) -->
          <div class="card">
            <div class="card-img-wrap">
              <span class="badge badge-gold card-badge">Royal Tombs</span>
              <img src="assets/images/attractions/rajas-tomb.jpg" alt="Raja's Tomb Gaddige Madikeri">
            </div>
            <div class="card-body">
              <h3 class="card-title">Raja's Tomb (Gaddige)</h3>
              <p class="card-text">
                Built in Muhammadan architectural style with central domes, these historic 1809 tombs house the royal remains of King Doddaveerarajendra and Lingarajendra.
              </p>
              <div style="margin-bottom: 1.25rem; font-size: 0.85rem; color: var(--color-accent); font-weight: 600;">
                Distance: ~2.5 km (7 mins drive)
              </div>
              <a href="attractions/rajas-tomb.html" class="btn btn-outline-dark btn-sm" style="width: 100%;">Read Full Visitor Guide &rarr;</a>
            </div>
          </div>
        </div>

        <div style="margin-top: 5rem;">
          {render_booking_form()}
        </div>
      </div>
    </section>
    """
    return render_page(
        title="Places to Visit Near Coorg Villa | Madikeri Sightseeing",
        description="Discover the best places to visit in Madikeri near Coorg Villa: Omkareshwara Temple, Raja's Seat, Abbey Falls, Madikeri Fort, and Raja's Tomb.",
        canonical_slug="places-to-visit-madikeri.html",
        body_content=body,
        active_tab="PLACES",
        root_path=""
    )

def build_location_page():
    body = f"""
    <div style="background-color: var(--color-primary-dark); color: #FFFFFF; padding: 4rem 0 3rem 0; text-align: center;">
      <div class="container">
        <span class="eyebrow" style="color: var(--color-accent-light);">Location & Directions</span>
        <h1 style="color: #FFFFFF; margin-top: 0.5rem;">Stay Near Omkareshwara Temple, Madikeri</h1>
        <p style="max-width: 680px; margin: 1rem auto 0 auto; color: rgba(255,255,255,0.85); font-size: 1.1rem;">
          Prime central location in Madikeri town, near the historic Omkareshwara Temple with simple highway access from Bengaluru, Mysuru, and Mangaluru.
        </p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="grid-2" style="gap: 3.5rem; align-items: flex-start; margin-bottom: 4rem;">
          <div>
            <span class="eyebrow">Central Advantage</span>
            <h2>How to Reach Coorg Villa</h2>
            <p style="margin-top: 1rem;">
              Coorg Villa is located in Madikeri, the headquarters and central hub of the Kodagu (Coorg) district. Our proximity to Omkareshwara Temple makes arriving and checking in straightforward.
            </p>
            
            <h4 style="margin-top: 1.75rem; color: var(--color-primary);">Road Routes from Major Hubs:</h4>
            <div style="display: flex; flex-direction: column; gap: 1rem; margin-top: 1rem;">
              <div style="background: var(--color-surface); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--color-border);">
                <strong>From Bengaluru (~255 km / 5.5 hrs):</strong>
                <p style="font-size: 0.9rem; color: var(--color-text-muted); margin-top: 0.3rem;">
                  Bengaluru &rarr; Mysuru Expressway &rarr; Hunsur &rarr; Kushalnagar &rarr; Madikeri town. Follow signs towards Omkareshwara Temple.
                </p>
              </div>

              <div style="background: var(--color-surface); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--color-border);">
                <strong>From Mysuru (~118 km / 2.5 hrs):</strong>
                <p style="font-size: 0.9rem; color: var(--color-text-muted); margin-top: 0.3rem;">
                  Mysuru &rarr; Bilikere &rarr; Hunsur &rarr; Kushalnagar &rarr; Madikeri.
                </p>
              </div>

              <div style="background: var(--color-surface); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--color-border);">
                <strong>From Mangaluru (~138 km / 3.5 hrs):</strong>
                <p style="font-size: 0.9rem; color: var(--color-text-muted); margin-top: 0.3rem;">
                  Mangaluru &rarr; Bantwal &rarr; Puttur &rarr; Sullia &rarr; Sampaje Ghat &rarr; Madikeri town centre.
                </p>
              </div>
            </div>

            <div style="margin-top: 2rem;">
              <a href="{PHONE_TEL}" class="btn btn-primary">Call for Exact Directions &rarr;</a>
            </div>
          </div>

          <div>
            <div style="background: var(--color-surface); padding: 1rem; border-radius: var(--radius-lg); border: 1px solid var(--color-border); box-shadow: var(--shadow-md);">
              <h3 style="font-size: 1.25rem; margin-bottom: 0.75rem;">Madikeri Town Map</h3>
              <iframe
                title="Madikeri, Coorg location map"
                src="https://www.google.com/maps?q=Madikeri%2C%20Karnataka&output=embed"
                width="100%"
                height="420"
                style="border:0;border-radius:12px; display:block;"
                loading="lazy"
                referrerpolicy="no-referrer-when-downgrade"
                allowfullscreen>
              </iframe>
              <p style="font-size: 0.85rem; color: var(--color-text-muted); margin-top: 0.75rem;">
                * Temporary Madikeri Town map. Contact us on WhatsApp/phone for current live Google Maps pin upon arrival.
              </p>
            </div>
          </div>
        </div>

        <div style="margin-top: 5rem;">
          {render_booking_form()}
        </div>
      </div>
    </section>
    """
    return render_page(
        title="Stay Near Omkareshwara Temple, Madikeri | Coorg Villa",
        description="Looking for accommodation near Omkareshwara Temple in Madikeri? Explore the location of Coorg Villa and enquire about availability.",
        canonical_slug="location.html",
        body_content=body,
        active_tab="LOCATION",
        root_path=""
    )

def build_about_page():
    body = f"""
    <div style="background-color: var(--color-primary-dark); color: #FFFFFF; padding: 4rem 0 3rem 0; text-align: center;">
      <div class="container">
        <span class="eyebrow" style="color: var(--color-accent-light);">Hospitality & Comfort</span>
        <h1 style="color: #FFFFFF; margin-top: 0.5rem;">About Coorg Villa</h1>
        <p style="max-width: 680px; margin: 1rem auto 0 auto; color: rgba(255,255,255,0.85); font-size: 1.1rem;">
          Our homestay in Madikeri offers genuine Kodagu warmth, spacious 2-bedroom villas, and prime central convenience.
        </p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="grid-2" style="align-items: center; gap: 3.5rem; margin-bottom: 4rem;">
          <div>
            <span class="eyebrow">Our Story</span>
            <h2>A True Home Away from Home in Madikeri</h2>
            <p style="margin-top: 1rem;">
              Coorg Villa was conceived to offer travellers to Kodagu an authentic, spacious alternative to sterile commercial hotels. Located just moments from the historic Omkareshwara Temple, our property provides four independent 2-bedroom villas that give families, groups, and couples the freedom to live and relax together in total privacy.
            </p>
            <p>
              We believe great homestay hospitality lies in the details: clean and comfortable beds, continuous hot water for refreshing showers, dedicated power backup so you are never left in the dark, reliable Wi-Fi, and courteous host support to help you discover the finest local spots in Madikeri.
            </p>
            <div style="display: flex; gap: 1rem; margin-top: 2rem; flex-wrap: wrap;">
              <a href="villas.html" class="btn btn-primary">Explore Our Villas &rarr;</a>
              <a href="contact.html" class="btn btn-outline-dark">Contact Our Hosts</a>
            </div>
          </div>
          <div class="card-img-wrap" style="border-radius: var(--radius-lg); aspect-ratio: 4/3; box-shadow: var(--shadow-lg);">
            <img src="assets/images/villas/town-villa-coorg-entrance-hallway.jpg" alt="Coorg Villa Corridor & Entrance">
          </div>
        </div>

        <!-- 3 Pillars of Hospitality -->
        <div class="grid-3" style="margin-top: 4rem;">
          <div class="card" style="padding: 2rem;">
            <div class="highlight-icon" style="margin-bottom: 1.25rem;">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
            </div>
            <h3 style="font-size: 1.2rem; margin-bottom: 0.6rem;">Central Location</h3>
            <p style="font-size: 0.9rem; color: var(--color-text-muted);">
              Situated right in Madikeri town near Omkareshwara Temple, avoiding the long nightly drives back to remote hills while remaining quiet and peaceful.
            </p>
          </div>

          <div class="card" style="padding: 2rem;">
            <div class="highlight-icon" style="margin-bottom: 1.25rem;">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
            </div>
            <h3 style="font-size: 1.2rem; margin-bottom: 0.6rem;">Independent Villas</h3>
            <p style="font-size: 0.9rem; color: var(--color-text-muted);">
              Each villa offers 2 private bedrooms, an exclusive living room, dining space, and attached bathrooms, accommodating 6–8 guests in comfort.
            </p>
          </div>

          <div class="card" style="padding: 2rem;">
            <div class="highlight-icon" style="margin-bottom: 1.25rem;">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
            </div>
            <h3 style="font-size: 1.2rem; margin-bottom: 0.6rem;">Direct Host Care</h3>
            <p style="font-size: 0.9rem; color: var(--color-text-muted);">
              Deal directly with genuine local hosts on phone and WhatsApp. No impersonal call centers, no surprise fees, and genuine travel guidance.
            </p>
          </div>
        </div>

        <div style="margin-top: 5rem;">
          {render_booking_form()}
        </div>
      </div>
    </section>
    """
    return render_page(
        title="About Coorg Villa – Our Homestay in Madikeri",
        description="Learn about Coorg Villa, our 4 spacious 2-bedroom villas, prime location near Omkareshwara Temple in Madikeri, and genuine Kodagu hospitality.",
        canonical_slug="about.html",
        body_content=body,
        active_tab="ABOUT",
        root_path=""
    )

def build_contact_page():
    body = f"""
    <div style="background-color: var(--color-primary-dark); color: #FFFFFF; padding: 4rem 0 3rem 0; text-align: center;">
      <div class="container">
        <span class="eyebrow" style="color: var(--color-accent-light);">Reach Out Directly</span>
        <h1 style="color: #FFFFFF; margin-top: 0.5rem;">Contact Coorg Villa</h1>
        <p style="max-width: 680px; margin: 1rem auto 0 auto; color: rgba(255,255,255,0.85); font-size: 1.1rem;">
          Call or WhatsApp our host team directly on {PHONE_RAW} for villa availability, special group rates, and directions.
        </p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="grid-2" style="gap: 3.5rem; margin-bottom: 4rem;">
          <div>
            <span class="eyebrow">Direct Booking Support</span>
            <h2>Get in Touch with Our Host</h2>
            <p style="margin-top: 1rem;">
              Whether you have questions about villa capacity, check-in arrangements, or would like to enquire about availability for your preferred travel dates, we are here to assist you promptly.
            </p>

            <div style="display: flex; flex-direction: column; gap: 1.5rem; margin-top: 2rem;">
              <div style="display: flex; gap: 1rem; align-items: flex-start;">
                <div class="highlight-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                </div>
                <div>
                  <h4 style="margin-bottom: 0.2rem;">Direct Phone Call</h4>
                  <a href="{PHONE_TEL}" style="font-size: 1.15rem; font-weight: 700; color: var(--color-primary);">{PHONE_DISPLAY}</a>
                  <p style="font-size: 0.85rem; color: var(--color-text-muted); margin-top: 0.2rem;">Available daily for instant queries & bookings.</p>
                </div>
              </div>

              <div style="display: flex; gap: 1rem; align-items: flex-start;">
                <div class="highlight-icon" style="background-color: rgba(37, 211, 102, 0.15); color: var(--color-whatsapp-dark);">
                  <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2ZM12.05 20.15C10.57 20.15 9.12 19.76 7.85 19.01L7.55 18.83L4.43 19.65L5.26 16.61L5.06 16.29C4.24 14.99 3.81 13.47 3.81 11.91C3.81 7.37 7.5 3.68 12.05 3.68C14.25 3.68 16.32 4.54 17.88 6.09C19.43 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.59 20.15 12.05 20.15ZM16.57 14.37C16.32 14.25 15.1 13.65 14.87 13.57C14.65 13.48 14.48 13.44 14.32 13.69C14.15 13.94 13.67 14.5 13.52 14.67C13.38 14.83 13.23 14.85 12.98 14.73C12.73 14.6 11.93 14.34 10.98 13.49C10.24 12.83 9.74 12.02 9.59 11.77C9.45 11.52 9.58 11.39 9.7 11.27C9.81 11.16 9.95 10.98 10.08 10.83C10.2 10.68 10.25 10.57 10.33 10.41C10.41 10.24 10.37 10.1 10.31 9.98C10.25 9.85 9.76 8.65 9.55 8.16C9.35 7.68 9.15 7.74 9 7.74H8.53C8.36 7.74 8.09 7.8 7.86 8.05C7.63 8.3 7 8.89 7 10.09C7 11.29 7.88 12.45 8 12.61C8.13 12.78 9.72 15.23 12.16 16.29C12.74 16.54 13.19 16.69 13.54 16.8C14.12 16.99 14.65 16.96 15.07 16.9C15.54 16.83 16.51 16.31 16.71 15.74C16.92 15.17 16.92 14.68 16.85 14.58C16.79 14.47 16.64 14.41 16.39 14.29L16.57 14.37Z"/></svg>
                </div>
                <div>
                  <h4 style="margin-bottom: 0.2rem;">WhatsApp Chat</h4>
                  <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" style="font-size: 1.15rem; font-weight: 700; color: var(--color-whatsapp);">{PHONE_DISPLAY}</a>
                  <p style="font-size: 0.85rem; color: var(--color-text-muted); margin-top: 0.2rem;">Instant response with availability, quotes & photos.</p>
                </div>
              </div>

              <div style="display: flex; gap: 1rem; align-items: flex-start;">
                <div class="highlight-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                </div>
                <div>
                  <h4 style="margin-bottom: 0.2rem;">Property Address</h4>
                  <p style="font-size: 0.95rem; color: var(--color-text);">
                    Near Omkareshwara Temple, Madikeri,<br>
                    Kodagu (Coorg), Karnataka - 571201
                  </p>
                </div>
              </div>
            </div>
          </div>

          <div>
            {render_booking_form()}
          </div>
        </div>
      </div>
    </section>
    """
    return render_page(
        title="Contact Coorg Villa | Madikeri Stay Booking",
        description="Call or WhatsApp Coorg Villa on 8277268934 for villa availability and booking enquiries in Madikeri, Coorg.",
        canonical_slug="contact.html",
        body_content=body,
        active_tab="CONTACT",
        root_path=""
    )

def build_faq_page():
    body = f"""
    <div style="background-color: var(--color-primary-dark); color: #FFFFFF; padding: 4rem 0 3rem 0; text-align: center;">
      <div class="container">
        <span class="eyebrow" style="color: var(--color-accent-light);">Common Enquiries</span>
        <h1 style="color: #FFFFFF; margin-top: 0.5rem;">Frequently Asked Questions</h1>
        <p style="max-width: 680px; margin: 1rem auto 0 auto; color: rgba(255,255,255,0.85); font-size: 1.1rem;">
          Find answers regarding booking terms, villa layouts, parking, extra beds, and local Madikeri attractions.
        </p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        {render_faq_accordions()}

        <div style="margin-top: 5rem;">
          {render_booking_form()}
        </div>
      </div>
    </section>
    """
    return render_page(
        title="Frequently Asked Questions About Our Madikeri Homestay | FAQ",
        description="Find answers to common questions about staying at Coorg Villa in Madikeri, including villa capacity, check-in, parking, and amenities.",
        canonical_slug="faq.html",
        body_content=body,
        active_tab="FAQ",
        root_path=""
    )

def build_privacy_policy_page():
    body = f"""
    <div style="background-color: var(--color-primary-dark); color: #FFFFFF; padding: 4rem 0 3rem 0; text-align: center;">
      <div class="container">
        <span class="eyebrow" style="color: var(--color-accent-light);">Transparency & Trust</span>
        <h1 style="color: #FFFFFF; margin-top: 0.5rem;">Privacy Policy & House Rules</h1>
        <p style="max-width: 680px; margin: 1rem auto 0 auto; color: rgba(255,255,255,0.85); font-size: 1.1rem;">
          Our guest privacy commitment and essential guidelines for a peaceful stay at Coorg Villa.
        </p>
      </div>
    </div>

    <section class="section">
      <div class="container" style="max-width: 860px;">
        <div style="background: var(--color-surface); padding: clamp(1.5rem, 4vw, 3rem); border-radius: var(--radius-lg); border: 1px solid var(--color-border); box-shadow: var(--shadow-sm);">
          <h2>Guest Privacy Policy</h2>
          <p style="margin-top: 1rem; color: var(--color-text-muted);">
            At Coorg Villa, we respect your privacy. Any personal information collected during enquiry or booking—including guest names, contact numbers, email addresses, and identification documents—is utilized strictly for confirming reservations, complying with local hospitality registration laws, and communicating with you regarding your stay. We do not sell or share personal data with external marketing third parties.
          </p>

          <h3 style="margin-top: 2rem;">Booking & Confirmation Terms</h3>
          <ul style="margin: 1rem 0 1.5rem 1.25rem; color: var(--color-text-muted); line-height: 1.7;">
            <li>Bookings are confirmed directly via phone or WhatsApp upon mutual agreement of dates, guest count, and advance payment if required.</li>
            <li>Valid government-issued photo ID (Aadhaar, Passport, Driving License) is required for all adult guests upon check-in as per regulatory norms.</li>
            <li>Standard check-in time is from 12:00 PM, and check-out time is by 11:00 AM. Early check-in or late check-out is subject to villa availability.</li>
          </ul>

          <h3 style="margin-top: 2rem;">Property House Rules</h3>
          <ul style="margin: 1rem 0 1.5rem 1.25rem; color: var(--color-text-muted); line-height: 1.7;">
            <li><strong>Residential Peace:</strong> Coorg Villa is situated in a quiet residential neighborhood near Omkareshwara Temple. We kindly request guests to observe quiet hours after 10:00 PM to respect neighboring residents and other staying families.</li>
            <li><strong>No Smoking Indoors:</strong> Smoking is strictly prohibited inside the bedrooms, living halls, and bathrooms. Dedicated outdoor smoking zones are provided.</li>
            <li><strong>Care for Villa Property:</strong> Guests are requested to treat the villa fixtures, electronics, furniture, and linens with care. Any intentional damage or missing items will be charged to the guest.</li>
            <li><strong>Vehicle Parking:</strong> On-premises parking is provided for guest convenience. Vehicles are parked at owner's discretion.</li>
          </ul>

          <div style="margin-top: 2.5rem; text-align: center;">
            <a href="contact.html" class="btn btn-primary">Have Questions? Contact Us &rarr;</a>
          </div>
        </div>
      </div>
    </section>
    """
    return render_page(
        title="Privacy Policy & House Rules | Coorg Villa",
        description="Read the guest privacy policy, booking terms, and house rules for staying at Coorg Villa in Madikeri.",
        canonical_slug="privacy-policy.html",
        body_content=body,
        active_tab="",
        root_path=""
    )

def build_attraction_page(slug, title, heading, badge, image, desc, details_html):
    body = f"""
    <div style="background-color: var(--color-primary-dark); color: #FFFFFF; padding: 4rem 0 3rem 0; text-align: center;">
      <div class="container">
        <span class="eyebrow" style="color: var(--color-accent-light);">Madikeri Sightseeing Guide</span>
        <h1 style="color: #FFFFFF; margin-top: 0.5rem;">{heading}</h1>
        <p style="max-width: 680px; margin: 1rem auto 0 auto; color: rgba(255,255,255,0.85); font-size: 1.1rem;">
          {desc}
        </p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="grid-2" style="align-items: center; gap: 3.5rem; margin-bottom: 4rem;">
          <div class="card-img-wrap" style="border-radius: var(--radius-lg); aspect-ratio: 4/3; box-shadow: var(--shadow-lg);">
            <img src="../assets/images/attractions/{image}" alt="{heading}">
          </div>
          <div>
            <span class="badge badge-gold" style="margin-bottom: 0.75rem;">{badge}</span>
            <h2>Visitor Information & Highlights</h2>
            {details_html}
            <div style="margin-top: 2rem; display: flex; gap: 1rem; flex-wrap: wrap;">
              <a href="../places-to-visit-madikeri.html" class="btn btn-outline-dark">&larr; All Attractions</a>
              <a href="../contact.html" class="btn btn-primary">Stay Near This Attraction &rarr;</a>
            </div>
          </div>
        </div>

        <div style="margin-top: 5rem;">
          {render_booking_form("../")}
        </div>
      </div>
    </section>
    """
    return render_page(
        title=f"{title} | Coorg Villa Guide",
        description=desc,
        canonical_slug=f"attractions/{slug}.html",
        body_content=body,
        active_tab="PLACES",
        root_path="../"
    )

def build_blog_index_page():
    articles = [
        ("Best Places to Visit in Madikeri Near the Town Centre", "A curated walking and short-drive guide to central Madikeri landmarks including Omkareshwara Temple, Raja's Seat, and the bustling local spice markets."),
        ("Omkareshwara Temple Madikeri – Complete Visitor Guide", "History, legend, unique Indo-Islamic architecture, and essential timing tips for visiting Kodagu's sacred Shiva shrine."),
        ("How to Choose a Family Homestay in Madikeri", "What discerning families should look for: private bedrooms, shared living halls, in-villa refrigerators, hot water, and safe parking."),
        ("Madikeri 2-Day Travel Itinerary for Weekend Travellers", "How to make the most of 48 hours in Coorg: viewpoints, waterfalls, coffee estate strolls, and authentic Kodava meals."),
        ("Hotels vs Homestays in Madikeri – Which Is Right for You?", "Comparing the privacy, space, and personal hospitality of a 2-bedroom villa homestay against conventional hotel rooms."),
        ("Where to Stay in Madikeri for a Family Trip", "Why central Madikeri stays offer superior safety, convenience, and time savings compared to remote forest resorts."),
        ("Best Time to Visit Madikeri and Coorg Weather Guide", "Monthly breakdown of Coorg's weather—monsoon mist, pleasant winter chill, and cool summer retreats."),
        ("What to Pack for a Coorg Weekend Trip", "Essential clothing, footwear, rain gear, and road-trip necessities for a comfortable vacation in Kodagu."),
        ("How to Reach Madikeri from Mysuru and Bengaluru", "Comprehensive highway route advice, road conditions, scenic stopovers, and travel times."),
        ("Group Stay in Coorg – Planning Accommodation for Friends & Families", "How our 4 villas accommodate up to 32 guests together while retaining private living halls and bedrooms.")
    ]

    cards_html = ""
    for title, excerpt in articles:
        cards_html += f"""
        <div class="card">
          <div class="card-body">
            <span class="badge badge-gold" style="margin-bottom: 0.6rem;">Travel Guide</span>
            <h3 class="card-title" style="font-size: 1.25rem;">{title}</h3>
            <p class="card-text">{excerpt}</p>
            <a href="../contact.html" style="color: var(--color-accent); font-weight: 600; font-size: 0.9rem;">
              Plan Your Stay &rarr;
            </a>
          </div>
        </div>
        """

    body = f"""
    <div style="background-color: var(--color-primary-dark); color: #FFFFFF; padding: 4rem 0 3rem 0; text-align: center;">
      <div class="container">
        <span class="eyebrow" style="color: var(--color-accent-light);">Coorg Travel Blog</span>
        <h1 style="color: #FFFFFF; margin-top: 0.5rem;">Coorg Travel Guides & Itineraries</h1>
        <p style="max-width: 680px; margin: 1rem auto 0 auto; color: rgba(255,255,255,0.85); font-size: 1.1rem;">
          Helpful travel insights, itineraries, and accommodation advice from the local hosts of Coorg Villa.
        </p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="grid-2" style="gap: 2rem;">
          {cards_html}
        </div>

        <div style="margin-top: 5rem;">
          {render_booking_form("../")}
        </div>
      </div>
    </section>
    """
    return render_page(
        title="Coorg Travel Guides & Madikeri Itineraries | Coorg Villa Blog",
        description="Read useful travel guides, 2-day Madikeri itineraries, family stay advice, and local sightseeing tips for planning your Coorg holiday.",
        canonical_slug="blog/index.html",
        body_content=body,
        active_tab="BLOG",
        root_path="../"
    )

def build_404_page():
    body = f"""
    <div style="padding: 6rem 0; text-align: center;">
      <div class="container" style="max-width: 600px;">
        <span class="eyebrow">Page Not Found</span>
        <h1 style="font-size: 4rem; margin: 0.5rem 0 1rem 0; color: var(--color-primary);">404</h1>
        <h2>Oops! This Page Wandered into the Mist</h2>
        <p style="color: var(--color-text-muted); margin: 1rem 0 2rem 0;">
          The page you are looking for might have been moved or does not exist. Let's guide you back to our comfortable villas.
        </p>
        <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
          <a href="index.html" class="btn btn-primary">Return to Homepage &rarr;</a>
          <a href="villas.html" class="btn btn-outline-dark">Explore Our Villas</a>
        </div>
      </div>
    </div>
    """
    return render_page(
        title="Page Not Found (404) | Coorg Villa",
        description="The page you are looking for cannot be found. Return to Coorg Villa homepage.",
        canonical_slug="404.html",
        body_content=body,
        active_tab="",
        root_path=""
    )

def build_sitemap():
    pages = [
        ("", "1.0", "daily"),
        ("villas.html", "0.9", "weekly"),
        ("amenities.html", "0.8", "monthly"),
        ("gallery.html", "0.8", "weekly"),
        ("family-stay-madikeri.html", "0.9", "weekly"),
        ("group-stay-madikeri.html", "0.9", "weekly"),
        ("couple-stay-madikeri.html", "0.8", "weekly"),
        ("places-to-visit-madikeri.html", "0.8", "weekly"),
        ("location.html", "0.8", "monthly"),
        ("about.html", "0.7", "monthly"),
        ("contact.html", "0.9", "weekly"),
        ("faq.html", "0.7", "monthly"),
        ("privacy-policy.html", "0.5", "yearly"),
        ("attractions/omkareshwara-temple.html", "0.8", "monthly"),
        ("attractions/rajas-seat.html", "0.8", "monthly"),
        ("attractions/madikeri-fort.html", "0.8", "monthly"),
        ("attractions/abbey-falls.html", "0.8", "monthly"),
        ("attractions/rajas-tomb.html", "0.7", "monthly"),
        ("blog/index.html", "0.8", "weekly")
    ]
    xml = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p, prio, freq in pages:
        loc = f"{SITE_URL}/{p}".rstrip('/')
        if p == "":
            loc = f"{SITE_URL}/"
        xml.append("  <url>")
        xml.append(f"    <loc>{loc}</loc>")
        xml.append(f"    <lastmod>2026-11-02</lastmod>")
        xml.append(f"    <changefreq>{freq}</changefreq>")
        xml.append(f"    <priority>{prio}</priority>")
        xml.append("  </url>")
    xml.append("</urlset>")
    return "\n".join(xml)

def build_robots():
    return f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""

def build_webmanifest():
    manifest = {
        "name": "Coorg Villa",
        "short_name": "Coorg Villa",
        "description": "Homestay in Madikeri, Coorg with four 2-bedroom villas near Omkareshwara Temple.",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#F8F5EF",
        "theme_color": "#17352B",
        "icons": [
            {
                "src": "/assets/icons/favicon.png",
                "sizes": "64x64",
                "type": "image/png"
            }
        ]
    }
    return json.dumps(manifest, indent=2)

def main():
    print("Building all pages for Coorg Villa...")

    # Top-level pages
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(build_homepage())
    print("✓ index.html")

    with open("villas.html", "w", encoding="utf-8") as f:
        f.write(build_villas_page())
    print("✓ villas.html")

    with open("amenities.html", "w", encoding="utf-8") as f:
        f.write(build_amenities_page())
    print("✓ amenities.html")

    with open("gallery.html", "w", encoding="utf-8") as f:
        f.write(build_gallery_page())
    print("✓ gallery.html")

    with open("family-stay-madikeri.html", "w", encoding="utf-8") as f:
        f.write(build_family_stay_page())
    print("✓ family-stay-madikeri.html")

    with open("group-stay-madikeri.html", "w", encoding="utf-8") as f:
        f.write(build_group_stay_page())
    print("✓ group-stay-madikeri.html")

    with open("couple-stay-madikeri.html", "w", encoding="utf-8") as f:
        f.write(build_couple_stay_page())
    print("✓ couple-stay-madikeri.html")

    with open("places-to-visit-madikeri.html", "w", encoding="utf-8") as f:
        f.write(build_places_page())
    print("✓ places-to-visit-madikeri.html")

    with open("location.html", "w", encoding="utf-8") as f:
        f.write(build_location_page())
    print("✓ location.html")

    with open("about.html", "w", encoding="utf-8") as f:
        f.write(build_about_page())
    print("✓ about.html")

    with open("contact.html", "w", encoding="utf-8") as f:
        f.write(build_contact_page())
    print("✓ contact.html")

    with open("faq.html", "w", encoding="utf-8") as f:
        f.write(build_faq_page())
    print("✓ faq.html")

    with open("privacy-policy.html", "w", encoding="utf-8") as f:
        f.write(build_privacy_policy_page())
    print("✓ privacy-policy.html")

    with open("404.html", "w", encoding="utf-8") as f:
        f.write(build_404_page())
    print("✓ 404.html")

    # Attractions
    attractions = [
        ("omkareshwara-temple", "Omkareshwara Temple Madikeri", "Omkareshwara Temple Madikeri – Historic Shiva Shrine",
         "Near Coorg Villa", "omkareshwara-temple.jpg",
         "Built in 1820 by King Lingarajendra II, Omkareshwara Temple is famous for its unique Gothic and Islamic dome architecture, peaceful holy water pond, and sacred linga.",
         """<p style="margin-top: 1rem;">Constructed in the early 19th century, Omkareshwara Temple is one of Madikeri's most revered spiritual landmarks. Uniquely combining Gothic and Islamic architectural elements, the temple resembles a peaceful dargah with a central dome and four corner minarets.</p>
            <p>At the center lies a scenic water pond housing freshwater fish where devotees can spend peaceful moments. Located just steps away from Coorg Villa, morning and evening temple visits are effortless for our staying guests.</p>"""),

        ("rajas-seat", "Raja's Seat Madikeri", "Raja's Seat Madikeri – Royal Sunset Viewpoint",
         "Panoramic Valley View", "rajas-seat.jpg",
         "The royal hilltop terrace where Kodagu kings enjoyed misty valley views and sunsets. Features manicured flower gardens, musical fountains, and panoramic vistas.",
         """<p style="margin-top: 1rem;">Raja's Seat (Seat of the Kings) was the favored scenic retreat of the Kodagu royalty. Overlooking rolling misty valleys and layered green hills, this viewpoint provides breathtaking sunset vistas.</p>
            <p>In the evenings, a musical fountain and seasonal floral displays attract visitors from across the country. Situated merely 1.8 km from Coorg Villa, you can easily catch the golden hour without worrying about night driving.</p>"""),

        ("madikeri-fort", "Madikeri Fort & Palace", "Madikeri Fort – Historic 17th-Century Heritage",
         "Kodagu Heritage", "madikeri-fort.jpg",
         "Originally constructed by Mudduraja and rebuilt in stone by Tipu Sultan, this ancient fort stands proudly in central Madikeri, housing a museum and colonial landmarks.",
         """<p style="margin-top: 1rem;">Madikeri Fort offers a journey through Coorg's storied history. Rebuilt with stone walls and battlements by Tipu Sultan, the fort premises feature two imposing life-sized stone elephants, an Anglican church turned archaeological museum, and panoramic views of Madikeri town.</p>
            <p>It is located only 1.2 km from Coorg Villa, making it an easy 4-minute drive or pleasant daytime walk.</p>"""),

        ("abbey-falls", "Abbey Falls Madikeri", "Abbey Falls – Spectacular Waterfall Amidst Coffee Plantations",
         "Lush Greenery", "abbey-falls.jpg",
         "A breathtaking 70-foot waterfall cascading over boulders amidst lush coffee estates and fragrant spice plantations in Madikeri.",
         """<p style="margin-top: 1rem;">Abbey Falls (Abbi Falls) is one of Coorg's most popular natural attractions. Nestled in private coffee and spice plantations, the water cascades down roughly 70 feet into a rocky gorge.</p>
            <p>Visitors walk along a scenic paved pathway surrounded by tall trees and pepper vines to reach the hanging viewing bridge. Located approximately 8.5 km from central Madikeri, it makes an ideal morning excursion from Coorg Villa.</p>"""),

        ("rajas-tomb", "Raja's Tomb (Gaddige)", "Raja's Tomb (Gaddige) – Royal Tombs of Kodagu",
         "Historic Monument", "rajas-tomb.jpg",
         "Gaddige houses the Indo-Saracenic domed royal tombs of King Doddaveerarajendra and Lingarajendra with intricate brass carvings and hillside panoramas.",
         """<p style="margin-top: 1rem;">Raja's Tomb, locally called Gaddige, features three striking Muhammadan-style domed structures with minarets honoring Kodagu rulers. The central tomb belongs to King Doddaveerarajendra and his queen, while the right tomb honors Lingarajendra.</p>
            <p>Situated on an elevated ridge about 2.5 km from Coorg Villa, Gaddige offers quiet heritage surroundings and picturesque views of Madikeri's gentle hills.</p>""")
    ]

    for slug, title, heading, badge, image, desc, details in attractions:
        filepath = os.path.join("attractions", f"{slug}.html")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(build_attraction_page(slug, title, heading, badge, image, desc, details))
        print(f"✓ {filepath}")

    # Blog index
    with open("blog/index.html", "w", encoding="utf-8") as f:
        f.write(build_blog_index_page())
    print("✓ blog/index.html")

    # Sitemap, Robots, Manifest, CNAME
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(build_sitemap())
    print("✓ sitemap.xml")

    with open("robots.txt", "w", encoding="utf-8") as f:
        f.write(build_robots())
    print("✓ robots.txt")

    with open("site.webmanifest", "w", encoding="utf-8") as f:
        f.write(build_webmanifest())
    print("✓ site.webmanifest")

    with open("CNAME", "w", encoding="utf-8") as f:
        f.write("thetownvillacoorg.com\n")
    print("✓ CNAME")

    print("\nAll 19 pages and assets built successfully!")

if __name__ == "__main__":
    main()
