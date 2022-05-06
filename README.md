# GoalTracker

## Motivation
It is difficult to keep track of the KPI set for the department and monitor each employee progress and on the other hand employees also will have a hard time keep track on their own while still working hard on their KPI. Hence this app is to assist both the manager and employee.

## What can this app do?
Manager can create goals for the deaprtment and assigned it to the employees via equally distributed or assigning to the specific members.

As for employee they can update their progress and also keep track on them.

## Build status
Currently in this app, it is at phase 1. I will want to be able to sort my data via the date for clarity and also to be able to click on department goals that shows all the employees goals allocation.

### List of things to work on

#### Must do (MVP)
Manager
1. Able to sign up as a manager and login as a manager. (Done)

2. Able to go in and see the top 3 latest department KPI goal. (Done without sorting)

3. Being able to create goals for the department:
  - Via equally distributed (Done)
  - Via allocating to specific department members (Done)

4. Able to see goals that are overdued in the archive tab. (Done)

5. Able to see all goals set for Department when click view all. (Done)

Employee
1. Able to sign up as a employee and login as a employee. (Done)

2. Able to go in and see the top 3 latest self KPI goal. (Done without sorting)

3. Being able to update the progress of their individual KPI goal. (Done)

4. Able to see goals that are overdued in the archive tab. (Done)

5. Able to see all goals set for self when click view all or Assigned Goals. (Done)

#### Can do (Stretch goals)
1. For manager to be able to see the employee individual goal distribution.

## Tech & Framework used

1. Vue.Js
- Props & Emit
- V-Functions
- router

2. Phython

3. Django
- SimpleJWT

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
