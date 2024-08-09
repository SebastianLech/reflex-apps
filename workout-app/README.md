# A Workout App

## Pages

### Home
Dashboard

### Users
- [ ] allow for new users
    - [x] button press to add new user
        - [x] form that lets you fill out data
            - [x] name
            - [x] height
            - [ ] weight - this is something that should be editible and tracked through time
            - [ ] age
    - [x] validate user entered data in real time
    - [x] insert new user into db
- [x] display new users
- [ ] edit user button
- [ ] delete user button


### Workouts
The workouts table will look something like

| Exercise ID | Username | Lift ID | Set | Reps | Weight | Time                | Lift Name                   |
|-------------|----------|---------|-----|------|--------|---------------------|-----------------------------|
|           1 | seb-lech |       1 |   1 |   10 |    225 | 06/08/2024 20:15:44 | Barbell Bench Press         |
|           1 | seb-lech |       1 |   2 |    9 |    225 | 06/08/2024 20:17:44 | Barbell Bench Press         |
|           1 | seb-lech |       1 |   3 |    8 |    225 | 06/08/2024 20:19:44 | Barbell Bench Press         |
|           1 | seb-lech |       2 |   1 |   10 |     65 | 06/08/2024 20:21:44 | Incline Dumbell Bench Press |
|           1 | seb-lech |       2 |   2 |   10 |     65 | 06/08/2024 20:23:44 | Incline Dumbell Bench Press |
|           1 | seb-lech |       2 |   3 |   10 |     65 | 06/08/2024 20:25:44 | Incline Dumbell Bench Press |
|           1 | seb-lech |       2 |   4 |   10 |     65 | 06/08/2024 20:27:44 | Incline Dumbell Bench Press |
|           1 | seb-lech |       4 |   1 |   10 | bw     | 06/08/2024 20:29:44 | Push Ups                    |
|           1 | seb-lech |       4 |   2 |   10 | bw     | 06/08/2024 20:31:44 | Push Ups                    |
|           1 | seb-lech |       4 |   3 |   10 | bw     | 06/08/2024 20:33:44 | Push Ups                    |
|           2 | seb-lech |       5 |   1 |   10 |    200 | 06/08/2024 22:34:44 | Squat                       |
|           2 | seb-lech |       5 |   2 |   10 |    200 | 06/08/2024 22:35:44 | Squat                       |
|           2 | seb-lech |       5 |   3 |   10 |    200 | 06/08/2024 22:36:44 | Squat                       |
|           2 | seb-lech |       5 |   4 |   10 |    200 | 06/08/2024 22:37:44 | Squat                       |
|           2 | seb-lech |       7 |   1 |   10 |     20 | 06/08/2024 22:38:44 | Splitsquat                  |
|           2 | seb-lech |       7 |   2 |   10 |     20 | 06/08/2024 22:39:44 | Splitsquat                  |
|           2 | seb-lech |       7 |   3 |   10 |     20 | 06/08/2024 22:40:44 | Splitsquat                  |
|           2 | seb-lech |       7 |   4 |   10 |     20 | 06/08/2024 22:41:44 | Splitsquat                  |


- [ ] button to create new workouts
    - requires definition of a _current_ workout
    - goes to exercise staging area
    - [ ] should ask for the user
- [ ] be able to add lifts to the current exercise
    - [ ] button to add lift in exercise staging area
        - [ ] button should create a form inline
- [ ] stage workouts
- [ ] save and commit them to the Exercises table

