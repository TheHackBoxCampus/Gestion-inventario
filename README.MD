## App de gestion de inventario a nivel basico

## Estructura del proyecto

Esta divido en 2 partes, la parte grafica y su respectiva API, 2 folders de la siguiente manera:

```
├── api/
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── schema.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── db.py
│   ├── modules/
│   │   └── module_name/
│   │       ├── model.py
│   │       ├── router.py
│   │       ├── controller.py
│   │       ├── schema.py
frontend/
├─package.json
├─ angular.json
├─ tsconfig.json
├─ src/
│  ├─ main.ts
│  ├─ index.html
│  ├─ styles.css
│  ├─ environments/
│  │  └─ environment.ts
│  └─ app/
│     ├─ app.config.ts
│     ├─ app.routes.ts
│     ├─ app.component.ts
│     ├─ app.component.html
│     ├─ app.component.css
│     ├─ services/
│     │  ├─ api.service.ts
│     │  └─ auth.service.ts
│     ├─ interceptors/
│     │  └─ auth.interceptor.ts
│     ├─ guards/
│     │  └─ auth.guard.ts
│     │  └─ auth.guard.ts
│     ├─ models/
│     │  ├─ producto.model.ts
│     │  └─ user.model.ts
│     └─ pages/
│        ├─ auth/
│        │  ├─ login.component.ts
│        │  ├─ login.html
│        │  ├─ login.css
│        │  ├─ register.component.ts
│        │  ├─ register.css
│        │  └─ register.html
│        ├─ products/
│        │  ├─ productos-list.component.ts
│        │  ├─ productos-list.component.html
│        │  ├─ producto-form.component.ts
│        │  └─ producto-form.component.html
│        └─ stats/
│           ├─ stats.component.ts
│           └─ stats.component.html
```

## Cada carpeta tiene un respectivo README.md revisa la informacion para saber el funcionamiento de la aplicacion 


