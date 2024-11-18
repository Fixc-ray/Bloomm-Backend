from models import db, Customer, Company, Category, Products, Order, Blog
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()

    category1 = Category(name="Makeup")
    category2 = Category(name="Hair Products")
    category3 = Category(name="SkinCare")
    category4 = Category(name="Fragrance")
    category5 = Category(name="Body Care")
    category6 = Category(name="Shaving Products")
    category7 = Category(name="Nail Care")
    category8 = Category(name="Men's Grooming")
    category9 = Category(name="Health & Wellness")
    category10 = Category(name="Tools & Accessories")
    category11 = Category(name="Organic")
    category12 = Category(name="Luxury")
    category13 = Category(name="Eyewear")
    category14 = Category(name="Teen Care")
    category15 = Category(name="Anti-aging")

    company1 = Company(name="Garnier")
    company2 = Company(name="L'Oreal")
    company3 = Company(name="Maybelline")
    company4 = Company(name="Sephora")
    company5 = Company(name="Dove")
    company6 = Company(name="Estee Lauder")
    company7 = Company(name="Bobbi Brown")
    company8 = Company(name="Urban Decay")
    company9 = Company(name="Cerave")
    company10 = Company(name="Clinique")
    company11 = Company(name="Lancome")
    company12 = Company(name="Neutrogena")
    company13 = Company(name="The Body Shop")
    company14 = Company(name="Tarte Cosmetics")
    company15 = Company(name="Vichy")
    company16 = Company(name="Mary Kay")
    company17 = Company(name="Revlon")
    company18 = Company(name="Kiehl's")
    company19 = Company(name="Burt's Bees")
    company20 = Company(name="Olay")
    company21 = Company(name="Aveda")

    product1 = Products(
        product_name="Face Cream",
        product_model="FC100",
        price=20.00,
        category=category3,
        company=company1,
        description="Garnier face creams are skincare products designed to hydrate, nourish, and improve skin appearance. They are formulated with ingredients like aloe vera and vitamin C.",
        photo_url="https://m.media-amazon.com/images/S/aplus-media-library-service-media/88282777-489d-43bd-b4b0-065c47641af3.__CR0,0,300,300_PT0_SX300_V1___.jpg"
    )

    product2 = Products(
        product_name="Shampoo",
        product_model="SH200",
        price=15.00,
        category=category2,
        company=company1,
        description="Garnier's shampoo hydrates and strengthens hair from root to tip, leaving it shiny and healthy without weighing it down.",
        photo_url="https://threebs.co/cdn/shop/products/garnier-sakura-white-pinkish-glow-foam-100ml-IMG1-20201016_300x300.jpg?v=1602783117"
    )

    product3 = Products(
        product_name="Anti-Aging Serum",
        product_model="AS300",
        price=40.00,
        category=category15,
        company=company9,
        description="Cerave Anti-aging serum is formulated with retinol to reduce the appearance of fine lines and wrinkles while supporting skin's natural moisture balance.",
        photo_url="https://image-delivery.nyc3.cdn.digitaloceanspaces.com/full/4ccce118f51337e069092df594b1391e.jpeg"
    )

    product4 = Products(
        product_name="Lipstick",
        product_model="LS400",
        price=25.00,
        category=category1,
        company=company2,
        description="L'Oreal’s lipstick offers long-lasting color and a smooth, hydrating formula to keep lips soft and vibrant.",
        photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSeiDRyDtFQSfuu5TZFa01Zcr5F7wJiHOwOOg&s"
    )

    product5 = Products(
        product_name="Moisturizing Lotion",
        product_model="ML500",
        price=18.00,
        category=category3,
        company=company9,
        description="Cerave’s Moisturizing Lotion is developed with dermatologists to provide essential moisture for dry and sensitive skin, without fragrance.",
        photo_url="https://threebs.co/cdn/shop/products/CER-TON-DAIL-355ml-IMG1-v2_300x300.jpg?v=1599143676"
    )

    product6 = Products(
        product_name="Foundation",
        product_model="FD600",
        price=28.00,
        category=category1,
        company=company3,
        description="Maybelline’s foundation offers full coverage while leaving a natural matte finish, suitable for all skin types.",
        photo_url="https://m.media-amazon.com/images/I/31QVkAicDAL._AC_SR300,300_.jpg"
    )

    product7 = Products(
        product_name="Body Butter",
        product_model="BB700",
        price=22.00,
        category=category5,
        company=company13,
        description="The Body Shop’s body butter is a rich, hydrating cream made with natural ingredients like shea butter and cocoa butter to deeply nourish dry skin.",
        photo_url="https://s.alicdn.com/@sc04/kf/H232040b071df43508eb90fe94ab06a89w.jpg_300x300.jpg"
    )

    product8 = Products(
        product_name="Shaving Gel",
        product_model="SG800",
        price=16.00,
        category=category6,
        company=company5,
        description="Dove's shaving gel creates a smooth, rich lather that glides over skin, providing a close, irritation-free shave.",
        photo_url="https://media.self.com/photos/57d8cddd50778cef321a615c/master/w_1600%2Cc_limit/HarrysDMC-300.jpg"
    )

    product9 = Products(
        product_name="Hand Cream",
        product_model="HC900",
        price=12.00,
        category=category3,
        company=company12,
        description="Neutrogena's hand cream is a fast-absorbing formula that helps relieve dry, cracked hands with a non-greasy finish.",
        photo_url="https://p7.hiclipart.com/preview/681/993/294/lotion-cream-neutrogena-clean-clear-exfoliation-pink-grapefruit-thumbnail.jpg"
    )

    product10 = Products(
        product_name="Perfume",
        product_model="PF1000",
        price=65.00,
        category=category4,
        company=company11,
        description="Lancome’s perfume offers a luxurious fragrance with floral and fruity notes, perfect for day or evening wear.",
        photo_url="https://cdn.jarrolds.co.uk/brands/lancome/25533-lancome-lveb-iris-reveal-duo-p4-e-070922%7Bw=300,h=300%7D.jpg"
    )

    product11 = Products(
        product_name="Hair Conditioner",
        product_model="HC1100",
        price=18.00,
        category=category2,
        company=company17,
        description="Revlon's hair conditioner nourishes and strengthens hair, leaving it soft, manageable, and shiny.",
        photo_url="https://imgfly.scarabresearch.com/w_300/https://www.salonsdirect.com/media/catalog/product/2/9/29544.jpg"
    )

    product12 = Products(
        product_name="Face Mask",
        product_model="FM1200",
        price=30.00,
        category=category3,
        company=company6,
        description="Estee Lauder's face mask revitalizes and replenishes skin, offering deep hydration and improving skin texture.",
        photo_url="https://cdn.jarrolds.co.uk/brands/estee-lauder/887167610620_2%7Bw=300,h=300%7D.jpg"
    )

    product13 = Products(
        product_name="Exfoliating Scrub",
        product_model="ES1300",
        price=22.00,
        category=category3,
        company=company10,
        description="Clinique's exfoliating scrub gently removes dead skin cells, leaving your skin feeling smooth and refreshed.",
        photo_url="https://static.thcdn.com/productimg/300/300/11144734-1145189031930384.jpg"
    )

    product14 = Products(
        product_name="Eyeliner",
        product_model="EL1400",
        price=18.00,
        category=category1,
        company=company7,
        description="Bobbi Brown’s eyeliner is designed for precise application, providing bold and long-lasting definition for your eyes.",
        photo_url="https://cdn.jarrolds.co.uk/brands/bobbi-brown/716170306131%E2%80%8B_0%7Bw=300,h=300%7D.jpg"
    )

    product15 = Products(
        product_name="Night Cream",
        product_model="NC1500",
        price=45.00,
        category=category15,
        company=company6,
        description="Estee Lauder’s night cream deeply nourishes and rejuvenates skin overnight, leaving you with a refreshed complexion.",
        photo_url="https://cdn.jarrolds.co.uk/brands/estee-lauder/2024/887167727823_5%7Bw=300,h=300%7D.jpg"
    )

    product16 = Products(
        product_name="Shampoo",
        product_model="SH1600",
        price=20.00,
        category=category2,
        company=company16,
        description="Mary Kay's shampoo nourishes and strengthens hair, promoting healthy growth while keeping your hair smooth and manageable.",
        photo_url="https://i.etsystatic.com/37439484/r/il/ba451b/6069782502/il_300x300.6069782502_32lj.jpg"
    )

    product17 = Products(
        product_name="Face Serum",
        product_model="FS1700",
        price=35.00,
        category=category3,
        company=company18,
        description="Kiehl’s face serum is a lightweight formula that hydrates and boosts skin’s natural radiance, with ingredients like vitamin C.",
        photo_url="https://www.kiehls.co.nz/dw/image/v2/BFZM_PRD/on/demandware.static/-/Sites-kiehls-nz-ng-Library/default/dw1c9aa0d9/images/articles/article-square-images/Vitamin-C.jpg?sw=300&sh=300&sm=cut&q=70"
    )

    product18 = Products(
        product_name="Fragrance Mist",
        product_model="FM1800",
        price=18.00,
        category=category4,
        company=company19,
        description="Burt's Bees' fragrance mist offers a natural, refreshing scent made from botanical ingredients, perfect for daily use.",
        photo_url="https://m.media-amazon.com/images/S/aplus-media/sota/38b1e84a-2aa6-4096-b17d-602baffe772f.__CR0,1,537,537_PT0_SX300_V1___.png"
    )

    product19 = Products(
        product_name="Hand & Body Lotion",
        product_model="HBL1900",
        price=25.00,
        category=category5,
        company=company20,
        description="Olay’s hand and body lotion nourishes skin, providing long-lasting moisture without leaving a greasy residue.",
        photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrdFdnyatjd8URqJHuMgRwPyfnDkchcBqGtA&s"
    )

    product20 = Products(
        product_name="Hair Styling Gel",
        product_model="HSG2000",
        price=12.00,
        category=category2,
        company=company2,
        description="L'Oreal’s hair styling gel provides strong hold and a sleek finish, ideal for sculpting and defining hairstyles.",
        photo_url="https://m.media-amazon.com/images/S/aplus-media/vc/9a2675e2-fae2-4067-9f8f-5a4f93d4f089.__CR0,0,300,300_PT0_SX300_V1___.jpg"
    )

    product21 = Products(
        product_name="Hand Wash",
        product_model="HW2100",
        price=10.00,
        category=category5,
        company=company14,
        description="Tarte’s hand wash is a gentle cleanser enriched with natural oils that leaves your hands feeling soft and refreshed.",
        photo_url="https://m.media-amazon.com/images/I/418YKGpZcdS._AC_SR300,300_.jpg"
    )
    
    product22 = Products(
        product_name="Shaving Foam",
        product_model="SF2200",
        price=17.00,
        category=category6,
        company=company8,
        description="Urban Decay’s shaving foam creates a rich, creamy lather that helps reduce irritation, leaving skin smooth after shaving.",
        photo_url="https://static.thcdn.com/productimg/300/300/11560495-7985155054542798.jpg"
    )

    product23 = Products(
        product_name="Nail Polish",
        product_model="NP2300",
        price=10.00,
        category=category7,
        company=company3,
        description="Maybelline’s nail polish offers vibrant color and long-lasting wear with a quick-drying formula.",
        photo_url="https://m.media-amazon.com/images/I/3182fmX-D4L._AC_SR300,300_.jpg"
    )

    product24 = Products(
        product_name="Moisturizing Facial Cream",
        product_model="MFC2400",
        price=38.00,
        category=category3,
        company=company12,
        description="Neutrogena’s moisturizing facial cream helps restore the skin’s natural moisture balance and leaves the skin feeling smooth and refreshed.",
        photo_url="https://m.media-amazon.com/images/I/71xSClnAFHL._AC_UF350,350_QL80_.jpg"
    )

    product25 = Products(
        product_name="Anti-Aging Serum",
        product_model="AAS2500",
        price=50.00,
        category=category15,
        company=company15,
        description="Vichy’s anti-aging serum reduces the appearance of fine lines and improves skin texture, leaving skin looking youthful and smooth.",
        photo_url="https://www.facethefuture.co.uk/cdn/shop/products/Vichy-Day-Cream-Neovadiol-Rose-Platinium-Day-Cream-000-3337875579919-Front.jpg?crop=center&height=300&v=1664532796&width=300"
    )
    
    blog1 = Blog(
        title="15 Essential Skincare Tips for Glowing Skin",
        content="""
        Taking care of your skin is essential for maintaining a radiant and youthful complexion. Here are 15 skincare tips that can help you achieve glowing skin every day:
        1. Cleanse Twice a Day – Cleanse your face every morning and night to remove impurities and makeup.
        2. Exfoliate Regularly – Exfoliating 2-3 times a week helps remove dead skin cells, leaving your skin smooth.
        3. Moisturize Daily – Even if you have oily skin, a light moisturizer can balance hydration and keep skin fresh.
        4. Apply SPF Every Day – Protect your skin from harmful UV rays with sunscreen, even on cloudy days.
        5. Drink Water – Staying hydrated helps keep your skin healthy and radiant from the inside out.
        6. Use Vitamin C – Vitamin C serums brighten the skin and help fight pigmentation and dark spots.
        7. Get Enough Sleep – Proper rest is crucial for skin rejuvenation.
        8. Eat a Balanced Diet – Incorporate antioxidant-rich fruits and vegetables for healthy, glowing skin.
        9. Avoid Touching Your Face – Keep your hands away from your face to reduce the spread of bacteria.
        10. Use a Humidifier – Adding moisture to dry air prevents your skin from becoming dehydrated.
        11. Avoid Stress – Stress can contribute to breakouts and dull skin. Practice relaxation techniques.
        12. Don’t Over-Wash Your Face – Over-cleansing can strip the skin of natural oils, leading to dryness.
        13. Use a Gentle Cleanser – Choose a mild cleanser that suits your skin type.
        14. Apply Toner – After cleansing, use a toner to balance your skin’s pH and tighten pores.
        15. Remove Makeup Before Bed – Always remove makeup at night to prevent clogged pores and breakouts.
        """,
        photo_url="https://www.shutterstock.com/image-photo/black-woman-dropper-facial-skincare-600nw-2226973499.jpg"
    )

    blog2 = Blog(
        title="Body Care Routine: 15 Must-Know Tips for Soft, Smooth Skin",
        content="""
        Taking care of your body skin is just as important as your facial skincare. Here are 15 simple tips to keep your body skin soft and smooth:
        1. Moisturize Right After Showering – Apply body lotion or oil while your skin is still damp to lock in moisture.
        2. Exfoliate Weekly – Use a body scrub or dry brush 1-2 times a week to remove dead skin cells.
        3. Stay Hydrated – Drinking plenty of water helps keep your skin hydrated and healthy.
        4. Avoid Hot Showers – Hot water can dry out your skin. Opt for lukewarm water instead.
        5. Use a Foot Cream – Pamper your feet with a nourishing cream to prevent cracks and dryness.
        6. Protect Your Skin from the Sun – Don’t forget to apply sunscreen to exposed skin when outdoors.
        7. Opt for a Body Oil – A rich oil provides deeper hydration than lotions, especially during the winter months.
        8. Gently Pat Dry – After showering, gently pat your skin dry with a towel to avoid irritation.
        9. Use a Body Scrub – Exfoliate your skin twice a week to remove dead skin and promote smoother texture.
        10. Drink Herbal Teas – Drinking herbal teas like chamomile or green tea can hydrate and detoxify your skin.
        11. Try a DIY Body Mask – Use natural ingredients like honey and coconut oil for a soothing at-home treatment.
        12. Use a Soothing Mist – A body mist with ingredients like aloe vera or lavender can help refresh your skin.
        13. Wear Soft Fabrics – Choose cotton or other gentle fabrics to avoid irritation.
        14. Apply a Firming Cream – For areas with cellulite or sagging, use a firming cream to promote elasticity.
        15. Sleep with Hydrating Gloves or Socks – Treat dry hands and feet by wearing moisturizing gloves or socks overnight.
        """,
        photo_url="https://www.fresh.com/dw/image/v2/BDJQ_PRD/on/demandware.static/-/Library-Sites-Fresh-SharedLibrary/default/dwe1e113eb/2024Holiday/H24_HolidayPt1_Noti.jpg"
    )

    blog3 = Blog(
        title="The Importance of Sunscreen in Your Skincare Routine",
        content="""
        Sunscreen is one of the most vital products in your skincare routine. Here's why it’s important and how to choose the right one for your skin:
        1. Prevents Premature Aging – UV rays accelerate the appearance of wrinkles and fine lines.
        2. Reduces Risk of Skin Cancer – Daily sun protection helps prevent skin damage and reduces the risk of skin cancer.
        3. Protects Against Hyperpigmentation – Sunscreen helps prevent dark spots and pigmentation.
        4. Use Broad-Spectrum SPF – Look for a sunscreen that protects against both UVA and UVB rays.
        5. Reapply Every 2 Hours – Sunscreen wears off throughout the day, so reapply regularly.
        6. Choose the Right SPF – Select SPF 30-50 for daily wear, and higher SPF for extended sun exposure.
        7. Don’t Skip Your Lips – Use a lip balm with SPF to protect your lips from sunburn.
        8. Apply Sunscreen Before Makeup – Let sunscreen absorb for 15-20 minutes before applying makeup.
        9. Wear Sunglasses – Protect the delicate skin around your eyes from sun damage by wearing sunglasses.
        10. Apply Generously – Ensure you apply enough sunscreen to cover your entire face and neck.
        11. Choose Water-Resistant Sunscreen – If you plan to swim or sweat, opt for water-resistant formulas.
        12. Use Sunscreen Even in Winter – UV rays can still cause damage in the winter months.
        13. Avoid Tanning – Don’t rely on tanning oils, as they can increase the risk of skin damage.
        14. Wear Protective Clothing – Choose wide-brimmed hats and long sleeves for added protection.
        15. Be Consistent – Apply sunscreen every morning, rain or shine, to maintain protection against UV damage.
        """,
        photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRn-rmm3e3uBDpd0FRO8lzlw0hpcfbWbx_7Vw&s"
    )

    blog4 = Blog(
        title="15 DIY Face Masks for Every Skin Type",
        content="""
        Treat your skin to these all-natural DIY face masks to address a variety of skincare needs:
        1. Honey & Yogurt Mask for Dry Skin – Honey hydrates while yogurt soothes and softens.
        2. Clay Mask for Oily Skin – Clay absorbs excess oil and helps with acne-prone skin.
        3. Avocado Mask for Sensitive Skin – Avocado nourishes and calms irritated skin.
        4. Lemon & Turmeric Mask for Brightening – This mask helps reduce dark spots and brighten the complexion.
        5. Oatmeal & Aloe Vera Mask for Soothing – Oatmeal soothes irritation and aloe vera promotes healing.
        6. Banana & Honey Mask for Hydration – Banana softens and nourishes the skin, while honey locks in moisture.
        7. Green Tea Mask for Acne – Green tea helps soothe inflammation and fight acne-causing bacteria.
        8. Papaya & Honey Mask for Radiance – Papaya exfoliates and brightens, while honey adds moisture.
        9. Coconut Oil & Coffee Scrub for Glowing Skin – Coffee exfoliates and helps to stimulate blood circulation.
        10. Egg White Mask for Tightening – Egg whites can tighten and firm the skin, reducing the appearance of pores.
        11. Cucumber & Aloe Mask for Soothing – Cucumber cools and hydrates, while aloe vera provides additional relief.
        12. Matcha & Honey Mask for Antioxidants – Matcha provides a boost of antioxidants that fight free radicals.
        13. Pumpkin & Yogurt Mask for Exfoliation – Pumpkin helps with cell turnover, revealing smoother skin.
        14. Milk & Honey Mask for Softness – Milk gently exfoliates, while honey hydrates for soft, glowing skin.
        15. Rosewater & Glycerin Mask for Moisture – Rosewater balances the skin, while glycerin locks in moisture.
        """,
        photo_url="https://static.toiimg.com/thumb/msid-84545582,width-400,resizemode-4/84545582.jpg"
    )

    blog5 = Blog(
        title="How to Choose the Right Skincare Products for Your Skin Type",
        content="""
        Your skin’s needs vary based on your skin type. Here’s a guide to choosing the right skincare products for your unique skin:
        1. For Oily Skin – Use gel-based cleansers, oil-free moisturizers, and non-comedogenic sunscreens.
        2. For Dry Skin – Opt for creamy cleansers, rich moisturizers, and hydrating serums with hyaluronic acid.
        3. For Sensitive Skin – Choose fragrance-free, hypoallergenic products with soothing ingredients like chamomile or aloe.
        4. For Combination Skin – Use lightweight moisturizers and balanced cleansers that target both dry and oily areas.
        5. For Acne-Prone Skin – Look for products with salicylic acid or benzoyl peroxide to treat and prevent breakouts.
        6. For Mature Skin – Use products that contain peptides, retinol, and vitamin C to reduce signs of aging.
        7. For Normal Skin – Use a gentle, balanced skincare routine with hydrating products.
        8. For Dehydrated Skin – Look for products with hyaluronic acid, glycerin, and ceramides to replenish moisture.
        9. Consider Non-Comedogenic – If you have acne-prone skin, always choose products labeled non-comedogenic.
        10. Read Labels – Pay attention to the ingredients in each product to make sure they suit your skin.
        11. Try a Skin Test – Always do a patch test before introducing a new product into your routine.
        12. Stick to a Routine – Consistency is key; don’t jump between products too quickly.
        13. Avoid Harsh Exfoliants – If you have sensitive skin, avoid products with abrasive scrubs or overly harsh ingredients.
        14. Prioritize Sunscreen – Choose a sunscreen that fits your skin type and offers broad-spectrum protection.
        15. Look for Multi-Tasking Products – Opt for products that can address multiple concerns at once, like anti-aging with hydration.
        """,
        photo_url="https://www.honest.com/dw/image/v2/BDBW_PRD/on/demandware.static/-/Library-Sites-HC-content/default/dw3f7b0b6b/2024/campaigns/derm-skincare-routines/SkincareQuiz_MarketingTile.jpg?sw=400"
    )

    blog6 = Blog(
        title="15 Best Anti-Aging Ingredients to Look for in Your Skincare",
        content="""
        Fight the signs of aging with these effective skincare ingredients:
        1. Retinol – Retinol speeds up cell turnover, reducing wrinkles and fine lines.
        2. Peptides – Peptides help firm and plump the skin, reducing sagging.
        3. Hyaluronic Acid – Hyaluronic acid hydrates and helps the skin retain moisture.
        4. Vitamin C – Brightens skin and boosts collagen production.
        5. Niacinamide – Reduces inflammation and improves skin texture.
        6. Alpha Hydroxy Acids (AHAs) – Exfoliate the skin, revealing a smoother, younger-looking complexion.
        7. Beta Hydroxy Acids (BHAs) – Help clear out clogged pores and improve skin texture.
        8. Antioxidants – Ingredients like green tea, resveratrol, and coenzyme Q10 fight free radical damage.
        9. Collagen – Collagen promotes skin elasticity and reduces wrinkles.
        10. Growth Factors – Stimulate collagen production and help the skin repair itself.
        11. Ceramides – Help to restore the skin's natural barrier and retain moisture.
        12. Squalane – A hydrating ingredient that helps prevent moisture loss.
        13. Vitamin E – An antioxidant that helps protect and repair skin damage.
        14. Zinc – Reduces inflammation and can help with acne and skin healing.
        15. Licorice Extract – Helps brighten skin and reduce dark spots and pigmentation.
        """,
        photo_url="https://www.kiehls.co.nz/dw/image/v2/BFZM_PRD/on/demandware.static/-/Sites-kiehls-nz-ng-Library/default/dw0742c663/images/articles/article-square-images/New%20Anti%20Aging%20Routine.jpg?sw=400&sh=400&sm=cut&q=70"
    )
    
    blog7 = Blog(
        title="How to Prevent and Treat Acne: 15 Key Tips",
        content="""
        Acne can be frustrating, but with the right care, it can be managed. Here’s how to prevent and treat acne effectively:
        1. Cleanse Gently – Use a gentle, non-drying cleanser to wash your face twice daily.
        2. Use Spot Treatments – Apply targeted treatments with benzoyl peroxide or salicylic acid.
        3. Avoid Picking at Pimples – Picking can introduce bacteria and cause scarring.
        4. Keep Your Skin Hydrated – Even acne-prone skin needs moisture to prevent overproduction of oil.
        5. Watch Your Diet – Some studies suggest a diet high in sugar and dairy may trigger breakouts.
        6. Exfoliate Regularly – Gentle exfoliation 1-2 times a week can prevent clogged pores.
        7. Try Retinoids – Retinoids can speed up cell turnover and help clear acne.
        8. Use Oil-Free Products – Look for oil-free moisturizers and makeup to avoid clogging pores.
        9. Stay Consistent with Your Routine – Acne treatments take time, so stick to your regimen.
        10. Be Gentle on Your Skin – Avoid harsh scrubbing, which can irritate your skin and worsen acne.
        11. Use Non-Comedogenic Products – Make sure the products you use are labeled as non-comedogenic (won’t clog pores).
        12. Get Enough Sleep – Poor sleep can lead to hormonal imbalance, which may trigger acne flare-ups.
        13. Protect Your Skin from the Sun – Use an oil-free sunscreen to protect acne-prone skin from UV damage.
        14. Manage Stress – Stress can trigger breakouts, so practice relaxation techniques to reduce stress.
        15. Consult a Dermatologist – If your acne is severe, a dermatologist can help with prescription treatments.
        """,
        photo_url="https://www.laroche-posay.com.au/dw/image/v2/BFZM_PRD/on/demandware.static/-/Sites-lrp-au-ng-Library/en_AU/dw605d23dc/articles/hyperpigmentation/pimple%20treatment%20products.jpg?sw=400&sh=400&sm=cut&q=70"
    )

    blog8 = Blog(
        title="Self-Care Sunday: 15 Tips for a Relaxing Skincare Routine",
        content="""
        Take some time every Sunday to pamper yourself and reset for the week ahead with this self-care skincare routine:
        1. Take a Warm Bath – Add essential oils or bath salts to relax your muscles.
        2. Exfoliate – Gently exfoliate to remove dead skin and improve circulation.
        3. Use a Face Mask – Choose a hydrating or calming mask for deep nourishment.
        4. Apply a Rich Moisturizer – Go for a heavy moisturizer to lock in hydration overnight.
        5. Relax and Unwind – Light some candles, meditate, or read your favorite book to reduce stress.
        6. Use a Body Scrub – Exfoliate your body to keep your skin smooth and soft.
        7. Apply a Foot Mask – Pamper your feet with a nourishing foot mask for smooth skin.
        8. Use a Hair Treatment – Apply a deep-conditioning treatment to your hair while you relax.
        9. Set the Mood – Create a peaceful atmosphere with calming music and dim lighting.
        10. Do a Facial Massage – Stimulate circulation and promote relaxation with a facial massage.
        11. Drink Herbal Tea – Sip on a calming herbal tea like chamomile or lavender to help you relax.
        12. Take a Break from Technology – Disconnect from screens to avoid stress and improve your well-being.
        13. Hydrate – Drink plenty of water throughout the day to keep your skin and body hydrated.
        14. Practice Mindfulness – Use meditation or deep breathing exercises to clear your mind.
        15. Write in a Journal – Reflect on your week and set positive intentions for the upcoming week.
        """,
        photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8GQbo06zi6OfmzMfubts5E7YaqfQsYgpgnQ&s"
    )

    blog9 = Blog(
        title="How to Maintain Healthy Hair: 15 Tips for Gorgeous Locks",
        content="""
        Beautiful hair starts with a good routine. Here are 15 tips to keep your hair healthy and shiny:
        1. Use a Sulfate-Free Shampoo – Sulfates can strip natural oils, so choose a gentle, sulfate-free formula.
        2. Condition Regularly – Conditioning helps nourish and hydrate your hair.
        3. Avoid Over-Washing – Washing your hair too often can cause dryness. Wash 2-3 times a week.
        4. Use Heat Protection – Always use a heat protectant before styling with hot tools.
        5. Trim Regularly – Regular trims prevent split ends and keep your hair looking healthy.
        6. Eat a Nutrient-Rich Diet – Include vitamins like biotin, vitamin D, and zinc to promote hair growth.
        7. Deep Condition Once a Week – Treat your hair to a deep conditioning treatment once a week.
        8. Drink Plenty of Water – Hydration is key for healthy hair. Drink water to nourish from the inside.
        9. Use a Wide-Tooth Comb – A wide-tooth comb is gentler on wet hair, preventing breakage.
        10. Avoid Tight Hairstyles – Tight ponytails or braids can cause hair damage or breakage.
        11. Protect Hair from Sun Damage – Use a UV protectant to shield your hair from the sun.
        12. Be Gentle When Drying – Pat your hair dry with a towel instead of rubbing it to avoid frizz.
        13. Sleep on Silk – A silk pillowcase reduces friction and prevents hair breakage while you sleep.
        14. Avoid Chemical Overload – Limit the use of harsh hair dyes and chemicals that can damage your strands.
        15. Don’t Skip Scalp Care – A healthy scalp is the foundation for healthy hair, so don’t forget to exfoliate and massage it.
        """,
        photo_url="https://photos.peopleimages.com/picture/202210/2528159-beauty-face-and-skincare-with-a-model-black-woman-in-studio-on-an-orange-background-with-a-joyful-or-carefree-expression.-cosmetics-skin-and-health-with-a-happy-young-female-posing-for-wellness-fit_400_400.jpg"
    )

    blog10 = Blog(
        title="15 Top Beauty Tips for a Natural, Effortless Look",
        content="""
        Looking beautiful doesn’t always require a lot of makeup. Here are 15 beauty tips to enhance your natural look:
        1. Embrace Minimal Makeup – Opt for tinted moisturizers, a bit of mascara, and a natural lip tint.
        2. Well-Groomed Eyebrows – Defined eyebrows can make a huge difference in framing your face.
        3. Hydrate Your Skin – Healthy, glowing skin requires proper hydration.
        4. Use a Highlighter – A subtle highlighter can give your skin a dewy, fresh appearance.
        5. Opt for Neutral Colors – Neutral tones for eyeshadow, blush, and lipstick enhance your natural features.
        6. Smile Often – A genuine smile makes you appear more beautiful instantly.
        7. Stay Active – Regular exercise increases blood flow and gives your skin a healthy glow.
        8. Use a Face Mist – Keep a refreshing mist on hand to hydrate and refresh your skin throughout the day.
        9. Take Care of Your Hands and Nails – Soft hands and well-manicured nails add to your natural beauty.
        10. Get Enough Sleep – Sleep is essential for your skin to repair and refresh.
        11. Use Lip Balm – Keep your lips hydrated and soft with a nourishing lip balm.
        12. Avoid Harsh Makeup Removers – Use a gentle, moisturizing makeup remover to avoid irritating your skin.
        13. Protect Your Skin – Apply sunscreen every day, even if you’re not wearing makeup.
        14. Clean Your Makeup Brushes – Regularly clean your brushes to avoid bacteria buildup.
        15. Keep a Good Posture – Standing tall and confident instantly makes you look more attractive.
        """,
        photo_url="https://pyxis.nymag.com/v1/imgs/747/bc6/7dab496c8d046f9728ac4c017ffb5ca5e3-Yara-Shahidi-WICLW.rsquare.w400.jpg"
    )
    
    blog11 = Blog(
        title="How to Get Rid of Dark Circles and Puffy Eyes",
        content="""
        Dark circles and puffiness around the eyes can be caused by various factors such as lack of sleep, stress, or genetics. Here’s how to treat them:
        1. Get Enough Sleep – Aim for 7-9 hours of sleep per night to reduce eye puffiness and dark circles.
        2. Apply Cold Compress – Use chilled cucumber slices or a cold, damp cloth to reduce swelling and inflammation.
        3. Use Eye Cream – Opt for an eye cream with ingredients like caffeine or peptides that target puffiness and dark circles.
        4. Stay Hydrated – Dehydration can worsen the appearance of dark circles, so drink plenty of water.
        5. Elevate Your Head – Sleeping with your head elevated prevents fluid retention around the eyes.
        6. Avoid Rubbing Your Eyes – Rubbing can irritate the delicate skin around your eyes and make puffiness worse.
        7. Use Green Tea Bags – Place chilled green tea bags over your eyes to reduce puffiness and dark circles.
        8. Try Aloe Vera Gel – Aloe vera soothes and hydrates the skin, helping to reduce dark circles.
        9. Apply Retinol – Retinol helps with collagen production and can reduce the appearance of fine lines under the eyes.
        10. Use Vitamin K Cream – Vitamin K may help lighten dark circles and improve blood circulation under the eyes.
        11. Reduce Salt Intake – Excessive sodium can cause water retention, leading to puffiness around the eyes.
        12. Protect Your Eyes from UV Rays – Always wear sunglasses and sunscreen to prevent skin damage around your eyes.
        13. Apply a Peptide-Infused Serum – Peptides help strengthen the skin around the eyes, reducing puffiness and dark circles.
        14. Get Regular Exercise – Exercise increases circulation, helping to reduce puffiness around the eyes.
        15. Use a Silk Pillowcase – A soft, silk pillowcase reduces friction on your delicate under-eye skin while sleeping.
        """,
        photo_url="https://s.alicdn.com/@sc04/kf/H3a5861efd9184932a5f4e388203a9fe30.jpg_300x300.jpg"
    )

    blog12 = Blog(
        title="How to Build a Skincare Routine for Sensitive Skin",
        content="""
        Sensitive skin requires special care to avoid irritation. Follow these steps to build a skincare routine that works:
        1. Choose Gentle Cleansers – Opt for non-foaming, fragrance-free cleansers to avoid stripping natural oils.
        2. Avoid Harsh Exfoliants – Skip physical scrubs and use mild exfoliants like enzyme-based masks.
        3. Hydrate, Hydrate, Hydrate – Use hydrating products like hyaluronic acid serums and soothing moisturizers.
        4. Patch Test New Products – Always patch-test new skincare products to ensure they won’t cause irritation.
        5. Use Sunscreen – Protect sensitive skin from harmful UV rays every day with a gentle, broad-spectrum sunscreen.
        6. Avoid Alcohol-Based Products – Alcohol can be drying and irritating to sensitive skin, so choose alcohol-free products.
        7. Incorporate Soothing Ingredients – Look for ingredients like chamomile, aloe vera, or calendula to calm the skin.
        8. Choose Fragrance-Free Products – Fragrances can trigger irritation, so opt for fragrance-free skincare options.
        9. Don’t Over-Exfoliate – Exfoliating too often can damage sensitive skin, so limit exfoliation to once or twice a week.
        10. Use a Humidifier – Dry indoor air can irritate sensitive skin, so use a humidifier to maintain moisture levels.
        11. Be Gentle with Skin Care – Avoid harsh rubbing and opt for gentle patting motions when applying products.
        12. Avoid Hot Showers – Hot water can strip the skin of moisture, so use lukewarm water instead.
        13. Choose Anti-Redness Products – For skin prone to redness, opt for products containing licorice extract or niacinamide.
        14. Moisturize Frequently – Sensitive skin needs constant hydration, so apply moisturizer regularly, especially after cleansing.
        15. Consult a Dermatologist – If your skin is frequently irritated, it’s a good idea to consult a dermatologist for personalized advice.
        """,
        photo_url="https://s.alicdn.com/@sc04/kf/H3469363b3aca453cb0da6b15c2377d62f.jpg_300x300.jpg"
    )

    blog13 = Blog(
        title="The Best Ingredients to Brighten Your Skin Naturally",
        content="""
        If you’re looking to brighten your complexion, there are several natural ingredients that can help. Here’s a list of the best:
        1. Vitamin C – Brightens skin by inhibiting melanin production and helps fight dark spots.
        2. Licorice Extract – Reduces hyperpigmentation and brightens dull skin.
        3. Niacinamide – This anti-inflammatory ingredient brightens skin tone and reduces redness.
        4. Alpha Arbutin – Known for lightening skin and reducing discoloration.
        5. Lactic Acid – A gentle exfoliant that removes dead skin cells, revealing a brighter complexion.
        6. Papaya Enzyme – Papaya contains natural enzymes that exfoliate the skin and brighten it naturally.
        7. Retinol – Helps to even out skin tone by increasing cell turnover and reducing dark spots.
        8. Rosehip Oil – Packed with Vitamin A and antioxidants, it helps brighten and regenerate skin.
        9. Green Tea Extract – Full of antioxidants, green tea can help reduce discoloration and redness in the skin.
        10. Mandelic Acid – A gentle exfoliant that works to brighten the skin without causing irritation.
        11. Kojic Acid – Known for its skin-brightening properties, kojic acid can fade dark spots and pigmentation.
        12. Mulberry Extract – Contains compounds that help reduce melanin production, brightening the skin naturally.
        13. Zinc – Zinc helps to reduce skin inflammation and aids in achieving an even skin tone.
        14. Turmeric – A natural anti-inflammatory and brightening agent, turmeric reduces skin pigmentation.
        15. Squalane – A hydrating ingredient that helps brighten the skin and maintains moisture levels.
        """,
        photo_url="https://cdn.shopify.com/s/files/1/0182/7451/7056/files/Why_Natural_Ingredients_Are_Best_For_Black_Skin_Unlock_The_Power_of_Nature_480x480.jpg?v=1685558170"
    )

    blog14 = Blog(
        title="How to Take Care of Your Skin During Winter",
        content="""
        Winter weather can be harsh on your skin. To keep your skin hydrated and protected, follow these winter skincare tips:
        1. Use a Humidifier – Dry air can rob your skin of moisture, so use a humidifier to keep skin hydrated.
        2. Switch to a Richer Moisturizer – Opt for thicker creams and oils to lock in moisture during the colder months.
        3. Exfoliate Gently – Dead skin buildup can prevent moisture from absorbing, so exfoliate lightly once a week.
        4. Protect Your Skin from Windburn – Wear a scarf or mask to protect your face from harsh winds.
        5. Don't Forget Your Lips – Use a nourishing lip balm to prevent chapped lips.
        6. Use a Nourishing Oil – Consider adding oils like argan or jojoba to your skincare routine for extra moisture.
        7. Avoid Hot Showers – Hot water can strip skin of its natural oils, so use lukewarm water when washing your face.
        8. Layer Your Skincare – Apply products in a layering sequence, starting with serums and ending with a rich moisturizer.
        9. Keep Your Skin Covered – Wear gloves, scarves, and hats to protect your skin from the harsh cold.
        10. Drink Warm Water – Sipping on warm water or herbal teas can help to hydrate your skin from within.
        11. Avoid Alcohol-Based Skincare – Alcohol can further dry out your skin, so stick to alcohol-free products.
        12. Opt for Gentle Cleaners – Use hydrating, non-stripping cleansers to avoid irritating your skin.
        13. Invest in a Good Night Cream – A thicker, richer night cream will help lock in moisture while you sleep.
        14. Don't Skip SPF – UV rays can still affect your skin during winter, so apply sunscreen daily.
        15. Take Warm, Not Hot, Baths – Keep your bathwater warm instead of hot to avoid stripping moisture from your skin.
        """,
        photo_url="https://i.etsystatic.com/8464954/r/il/422ed0/5420992556/il_300x300.5420992556_dwgl.jpg"
    )   

    blog15 = Blog(
        title="How to Get Flawless Skin: Tips for Every Skin Type",
        content="""
        Achieving flawless skin is a goal for many, and with the right approach, it’s possible. Here’s how to get glowing skin, no matter your skin type:
        1. Know Your Skin Type – Understanding your skin’s needs is the first step to choosing the right products.
        2. Keep Your Skin Hydrated – Moisturization is key for all skin types, whether oily, dry, or combination.
        3. Regular Exfoliation – Exfoliating helps reveal fresh skin and can treat skin texture issues.
        4. Use Targeted Treatments – Whether it’s for acne, dark spots, or fine lines, choose treatments that address your specific concerns.
        5. Consistency is Key – Stick to a skincare routine, as results take time, and consistency leads to the best results.
        6. Healthy Lifestyle Choices – Eating well, drinking water, and getting enough sleep can improve your skin’s appearance.
        7. Use Non-Comedogenic Products – If you have acne-prone skin, ensure your skincare products are non-comedogenic.
        8. Be Gentle on Your Skin – Avoid harsh scrubbing or aggressive product application.
        9. Apply Sunscreen Daily – Protect your skin from harmful UV rays by using sunscreen every morning.
        """,
        photo_url="https://hips.hearstapps.com/hmg-prod/images/flawlessskin-1589384044.png?crop=0.5xw:1xh;center,top&resize=640:*"
    )
    
    db.session.add_all([category1, category2, category3, category4, category5, category6, category7, category8, category9, category10, category11, category12, category13, category14, category15,
                        company1, company2, company3, company4, company5, company6, company7, company8, company9, company10, company11, company12, company13, company14, company15, company16,
                        company17, company18, company19, company20, company21,
                        product1, product2, product3, product4, product5, product6, product7, product8, product9, product10, product11, product12, product13, product14, product15, product16,
                        product17, product18, product19, product20, product21, product22, product23, product24, product25,
                        blog1, blog2, blog3, blog4, blog5, blog6, blog7, blog8, blog9, blog10, blog11, blog12, blog13, blog14, blog15])

    db.session.commit()

    print("Database seeded successfully")
