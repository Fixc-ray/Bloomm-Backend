from models import db, Customer, Company, Category, Products, Order
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
        photo_url=""
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

    db.session.add_all([category1, category2, category3, category4, category5, category6, category7, category8, category9, category10, category11, category12, category13, category14, category15,
                       company1, company2, company3, company4, company5, company6, company7, company8, company9, company10, company11, company12, company13, company14, company15, company16,
                       company17, company18, company19, company20, company21,
                       product1, product2, product3, product4, product5, product6, product7, product8, product9, product10, product11, product12, product13, product14, product15, product16,
                       product17, product18, product19, product20, product21, product22, product23, product24, product25])

    db.session.commit()

    print("Database seeded successfully")
