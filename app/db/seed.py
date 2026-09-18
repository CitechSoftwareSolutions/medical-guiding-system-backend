from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.models.role import Role, Permission, RolePermission
from app.models.document import Category
from app.models.subscription import Plan
from app.models.navigation import NavigationItem

DEFAULT_ROLES = [
    {"name": "Admin", "description": "System administrator with full access"},
    {"name": "Owner", "description": "Platform/Organization owner doctor"},
    {"name": "Doctor", "description": "Medical educator/doctor uploading resources and managing plans"},
    {"name": "Student", "description": "Medical student studying and accessing educational material"},
]

DEFAULT_PERMISSIONS = [
    {"name": "ViewDocument", "description": "View document metadata and preview"},
    {"name": "UploadDocument", "description": "Upload new medical/educational documents"},
    {"name": "DeleteDocument", "description": "Delete uploaded documents"},
    {"name": "DownloadDocument", "description": "Download full document contents"},
    {"name": "ManageStudents", "description": "View and manage student profiles and access"},
    {"name": "ManageDoctors", "description": "Manage doctor accounts and profiles"},
    {"name": "CreatePlan", "description": "Create and update subscription plans"},
    {"name": "ManageSubscription", "description": "Purchase, renew, or cancel subscriptions"},
    {"name": "UseChatbot", "description": "Interact with AI medical guidance chatbot"},
    {"name": "UsePremiumChatbot", "description": "Extended AI usage quota and specialized guidance"},
]

ROLE_PERMISSIONS_MAP = {
    "Admin": [p["name"] for p in DEFAULT_PERMISSIONS],
    "Owner": [p["name"] for p in DEFAULT_PERMISSIONS],
    "Doctor": [
        "ViewDocument",
        "UploadDocument",
        "DeleteDocument",
        "DownloadDocument",
        "ManageStudents",
        "CreatePlan",
    ],
    "Student": [
        "ViewDocument",
        "DownloadDocument",
        "ManageSubscription",
        "UseChatbot",
        "UsePremiumChatbot",
    ],
}

DEFAULT_CATEGORIES = [
    {"name": "Anatomy", "description": "Human gross and microscopic anatomy, histology, and embryology"},
    {"name": "Physiology", "description": "Human organ systems and physiological mechanisms"},
    {"name": "Pathology", "description": "General and systemic disease pathology and diagnostic markers"},
    {"name": "Pharmacology", "description": "Drug classes, mechanisms of action, pharmacokinetics, and toxicities"},
    {"name": "Internal Medicine", "description": "Clinical cases, diagnostic algorithms, and therapeutic guidelines"},
    {"name": "Surgery", "description": "Surgical techniques, operative notes, and perioperative care"},
]

DEFAULT_PLANS = [
    {
        "name": "Free Starter",
        "price": 0.00,
        "duration_days": 365,
        "description": "Access to all free documents and basic clinical guidance.",
        "features": [
            "Access to all Free core documents",
            "Basic clinical guidance consultation",
            "Standard community forum access",
            "View public clinical categories",
        ],
    },
    {
        "name": "Pro Monthly",
        "price": 29.00,
        "duration_days": 30,
        "description": "Full access to all premium documents and extended diagnostic consultation.",
        "features": [
            "Full access to 300+ Pro clinical documents",
            "Unlimited Clinical Guidance consultation",
            "Detailed examination notes & auscultation guides",
            "Direct doctor access request entitlement",
            "Priority student support",
        ],
    },
    {
        "name": "Premium Annual",
        "price": 199.00,
        "duration_days": 365,
        "description": "Complete 1-year unlimited access to all platform materials and priority support.",
        "features": [
            "Everything in Pro Monthly plan",
            "Full 365 days unlimited VIP access",
            "Exclusive high-yield exam preparation packages",
            "Direct clinical mentor messaging & webinars",
            "Official certificate of completion",
        ],
    },
]

DEFAULT_NAVIGATION_ITEMS = [
    # Top Navbar
    {"title": "Home", "path": "/", "icon": "Home", "menu_type": "top_navbar", "target_role": "all", "display_order": 1},
    {"title": "About", "path": "/about", "icon": "Info", "menu_type": "top_navbar", "target_role": "all", "display_order": 2},
    {"title": "Services", "path": "/services", "icon": "Activity", "menu_type": "top_navbar", "target_role": "all", "display_order": 3},
    {"title": "Contact", "path": "/contact", "icon": "Phone", "menu_type": "top_navbar", "target_role": "all", "display_order": 4},
    # Sidebar Student
    {"title": "Dashboard", "path": "/dashboard", "icon": "LayoutDashboard", "menu_type": "sidebar_student", "target_role": "student", "display_order": 1},
    {"title": "Resources", "path": "/documents", "icon": "BookOpen", "menu_type": "sidebar_student", "target_role": "student", "display_order": 2},
    {"title": "Clinical Guidance", "path": "/chat", "icon": "MessageSquare", "menu_type": "sidebar_student", "target_role": "student", "display_order": 3},
    {"title": "Plans", "path": "/plans", "icon": "CreditCard", "menu_type": "sidebar_student", "target_role": "student", "display_order": 4},
    # Sidebar Doctor
    {"title": "Dashboard", "path": "/doctor/dashboard", "icon": "LayoutDashboard", "menu_type": "sidebar_doctor", "target_role": "doctor", "display_order": 1},
    {"title": "Documents", "path": "/doctor/documents", "icon": "FileText", "menu_type": "sidebar_doctor", "target_role": "doctor", "display_order": 2},
    {"title": "Student Access", "path": "/doctor/grant-access", "icon": "UserCheck", "menu_type": "sidebar_doctor", "target_role": "doctor", "display_order": 3},
    {"title": "Plans", "path": "/plans", "icon": "CreditCard", "menu_type": "sidebar_doctor", "target_role": "doctor", "display_order": 4},
    # Sidebar Admin
    {"title": "Dashboard", "path": "/admin/users", "icon": "LayoutDashboard", "menu_type": "sidebar_admin", "target_role": "admin", "display_order": 1},
    {"title": "Audit Logs", "path": "/admin/audit-logs", "icon": "FileText", "menu_type": "sidebar_admin", "target_role": "admin", "display_order": 2},
    {"title": "Documents", "path": "/doctor/documents", "icon": "BookOpen", "menu_type": "sidebar_admin", "target_role": "admin", "display_order": 3},
    {"title": "Student Access", "path": "/doctor/grant-access", "icon": "UserCheck", "menu_type": "sidebar_admin", "target_role": "admin", "display_order": 4},
]


def seed_database(db: Session) -> None:
    # 1. Roles
    role_map = {}
    for r_data in DEFAULT_ROLES:
        role = db.scalar(select(Role).where(Role.name == r_data["name"]))
        if not role:
            role = Role(name=r_data["name"], description=r_data["description"])
            db.add(role)
            db.flush()
        role_map[r_data["name"]] = role

    # 2. Permissions
    perm_map = {}
    for p_data in DEFAULT_PERMISSIONS:
        perm = db.scalar(select(Permission).where(Permission.name == p_data["name"]))
        if not perm:
            perm = Permission(name=p_data["name"], description=p_data["description"])
            db.add(perm)
            db.flush()
        perm_map[p_data["name"]] = perm

    # 3. RolePermissions
    for role_name, perm_names in ROLE_PERMISSIONS_MAP.items():
        role = role_map.get(role_name)
        if not role:
            continue
        for p_name in perm_names:
            perm = perm_map.get(p_name)
            if not perm:
                continue
            existing = db.scalar(
                select(RolePermission).where(
                    RolePermission.role_id == role.id,
                    RolePermission.permission_id == perm.id,
                )
            )
            if not existing:
                db.add(RolePermission(role_id=role.id, permission_id=perm.id))

    # 4. Categories
    for c_data in DEFAULT_CATEGORIES:
        cat = db.scalar(select(Category).where(Category.name == c_data["name"]))
        if not cat:
            cat = Category(name=c_data["name"], description=c_data["description"])
            db.add(cat)

    # 5. Default Plans
    for p_data in DEFAULT_PLANS:
        plan = db.scalar(select(Plan).where(Plan.name == p_data["name"]))
        if not plan:
            plan = Plan(
                name=p_data["name"],
                price=p_data["price"],
                duration_days=p_data["duration_days"],
                description=p_data["description"],
                features=p_data.get("features"),
                status="active",
            )
            db.add(plan)
        else:
            plan.features = p_data.get("features")
            plan.description = p_data.get("description")

    # 6. Default Navigation Items
    for n_data in DEFAULT_NAVIGATION_ITEMS:
        item = db.scalar(
            select(NavigationItem).where(
                NavigationItem.menu_type == n_data["menu_type"],
                NavigationItem.path == n_data["path"],
            )
        )
        if not item:
            item = NavigationItem(
                title=n_data["title"],
                path=n_data["path"],
                icon=n_data["icon"],
                menu_type=n_data["menu_type"],
                target_role=n_data["target_role"],
                display_order=n_data["display_order"],
                is_active=True,
            )
            db.add(item)
        else:
            item.title = n_data["title"]
            item.icon = n_data["icon"]
            item.display_order = n_data["display_order"]

    db.commit()


if __name__ == "__main__":
    db = SessionLocal()
    try:
        seed_database(db)
        print("Database seeded successfully with roles, permissions, categories, plans, and navigation items.")
    finally:
        db.close()
