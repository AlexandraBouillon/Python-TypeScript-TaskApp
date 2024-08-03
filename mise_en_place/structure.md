
task-app/
├── backend/
│   ├── venv/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── task.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── task_routes.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── task_service.py
│   │   └── utils/
│   │       ├── __init__.py
│   │       ├── database.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   │   ├── TaskForm.tsx
│   │   │   ├── TaskList.tsx
│   │   │   └── TaskItem.tsx
│   │   ├── features/
│   │   │   ├── tasks/
│   │   │   │   ├── taskSlice.ts
│   │   │   │   └── taskAPI.ts
│   │   ├── pages/
│   │   │   ├── HomePage.tsx
│   │   │   └── TaskPage.tsx
│   │   ├── redux/
│   │   │   ├── store.ts
│   │   │   └── rootReducer.ts
│   │   ├── types/
│   │   │   ├── taskTypes.ts
│   │   ├── App.tsx
│   │   ├── index.tsx
│   │   ├── setupTests.ts
│   │   └── utils/
│   │       ├── api.ts
│   ├── .env
│   ├── package.json
│   ├── tsconfig.json
│   ├── cypress.json
│   ├── cypress/
│   │   ├── integration/
│   │   │   └── task.spec.ts
│   │   ├── fixtures/
│   │   └── support/
│   │       ├── commands.ts
│   │       └── index.ts
│   ├── Dockerfile
│   └── README.md
├── docker-compose.yml
└── .gitignore