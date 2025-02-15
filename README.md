using https://holidayapi.com/docs

the frontend folder is the executable api for holidayApi
the test folder is the testcase for frontend

| test_api     | testcase                                     | description                                          |
| ------------ | -------------------------------------------- | ---------------------------------------------------- |
| v1/holidays  | test 10/10 can find TW national day          | use country/month/day to find correct holiday        |
| v1/holidays  | test 10/10 with us cant find TW national day | use country/month/day to find holiday                |
| v1/holidays  | test wrong country                           | use wrong country to check error status              |
| v1/holidays  | previous cant be with upcoming               | use both previous and upcoming to check error status |
| v1/holidays  | search holiday                               | check search holiday function is correct             |
| v1/holidays  | test previous function                       | check previous holiday function is correct           |
| v1/holidays  | test upcoming function                       | check upcoming holiday function is correct           |
| v1/countries | test normal use                              | check country function is correct                    |
| v1/countries | test wrong country                           | check wrong country cant find any data               |
| v1/countries | test search                                  | check search country function is correct             |
