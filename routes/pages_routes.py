from flask import Blueprint, render_template, request, redirect, url_for, session
from aurora.models import Product

pages_bp = Blueprint("pages", __name__)

@pages_bp.route("/")
def landingpage():
    return render_template("landingpage.html")

@pages_bp.route("/about")
def about():
    return render_template("about.html")

@pages_bp.get("/products")
def products():
    items = Product.query.order_by(Product.id.asc()).all()
    return render_template("products.html", items=items)

@pages_bp.route("/cart")
def cart():
    cart_items = session.get("cart", [])
    total = 0.0
    for it in cart_items:
        total += float(it.get("price", 0)) * int(it.get("qty", 1))
    return render_template("cart.html", cart_items=cart_items, total=total)

@pages_bp.route("/add_to_cart/<int:item_id>", methods=["POST"])
def add_to_cart(item_id):
    p = Product.query.get_or_404(item_id)

    cart_items = session.get("cart", [])

    for it in cart_items:
        if it.get("id") == p.id:
            it["qty"] = int(it.get("qty", 1)) + 1
            session["cart"] = cart_items
            session.modified = True
            return redirect(url_for("pages.cart"))

    cart_items.append({
        "id": p.id,
        "title": p.title,
        "price": float(p.price) if p.price is not None else 0.0,
        "image_url": p.image_url,
        "qty": 1
    })

    session["cart"] = cart_items
    session.modified = True
    return redirect(url_for("pages.cart"))

@pages_bp.route("/remove_from_cart/<int:item_id>", methods=["POST"])
def remove_from_cart(item_id):
    cart_items = session.get("cart", [])
    cart_items = [it for it in cart_items if it.get("id") != item_id]
    session["cart"] = cart_items
    session.modified = True
    return redirect(url_for("pages.cart"))

@pages_bp.route("/signin", methods=["GET", "POST"])
def signin():
    return render_template("signin.html")

@pages_bp.route("/category/<name>")
def category(name):
    return render_template("category.html", name=name)

@pages_bp.route("/search")
def search():
    q = (request.args.get("q") or "").strip()
    return f"Search: {q}"
