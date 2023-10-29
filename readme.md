# Sustain-a-hack GUTS hackathon challenge

## The problem:
**Convince Cole Goode to care about the environment and change his behaviors accordingly!**

## Our solution:
<!-- ### Ecosteps! -->
![Alt text](https://github.com/EmranMR/EcoSteps-GUTS-Hackathon/blob/467c36b2f7515d021b5161b1793ecfd0c12894a6/public/images/image-1.png)
![Alt text](https://github.com/EmranMR/EcoSteps-GUTS-Hackathon/blob/467c36b2f7515d021b5161b1793ecfd0c12894a6/public/images/EcoSteps_logo.png)
A multifplatform web app which tracks a user’s steps and weight and publishes an embarrassing post to their social media and donates money to an environmental charity of their choice if they don’t meet a daily threshold. On the flipside, if a user does meet a given daily streak, they also get to donate money to an environmental charity of their choice giving them a dopamine hit and rush of endorphins!

## Environmental impact:
![Alt text](https://www.confectionerynews.com/var/wrbm_gb_food_pharma/storage/images/publications/food-beverage-nutrition/confectionerynews.com/article/2018/03/15/what-is-chocolate-s-biggest-environmental-impact/7974393-1-eng-GB/What-is-chocolate-s-biggest-environmental-impact.jpg)
- Donation to environmental charities
- Encourages walking over use of environmentally damaging transport modalities
- Walking as a healthy behaviours may compound into other healthy behaviours such as eating a more plant-based diet, which in turn has a significant environmental impact
- A healthier population drives economic productivity increasing capital available for environmental investment

## Technologies used:
- Open AI DALLE3 for logo generation
- Laravel PHP framework website backend/frontend: 🤩
  * TailwindCSS
  * Chart.js
  * Vitejs
- Python backend to connect with:
  * Google fit API to obtain user’s step count and weight
  * Mastodon API to post to user’s account
  * Push, pull and update data to database
- Firebase firestore database to store user data and allow Laravel frontend to access it

## Accessibility features:
![Alt text](https://github.com/EmranMR/EcoSteps-GUTS-Hackathon/blob/467c36b2f7515d021b5161b1793ecfd0c12894a6/public/images/image-4.png)
- Takes into account partially sighted users and those with other visual impairments by ensuring all page elements have alt txt
- Responsive front end web design to allow for access via multiple platforms and screen sizes
- Ability to interface with different health data i.e. not only steps to take into account for example users with limited mobility or wheelchair users

## Future features to be implemented:
![Alt text](https://github.com/EmranMR/EcoSteps-GUTS-Hackathon/blob/467c36b2f7515d021b5161b1793ecfd0c12894a6/public/images/image-3.png)
- Add further health data tracking to further take into account accessibility e.g. heart rate to take into account any form of exercise
- Continue improving UI to add e.g. github-style streak tracker
- Add further carrots to our mostly stick-centric model e.g. achievement badges, rewards system such as free t shirts (made of sustainably sourced materials)
- Finish connecting the frontend to the database

## Scaling to production ready codebase:
![Alt text](https://github.com/EmranMR/EcoSteps-GUTS-Hackathon/blob/467c36b2f7515d021b5161b1793ecfd0c12894a6/public/images/image-2.png)
- Integrate with Verint Da Vinci AI to analyze user trends to provide personalized advice, generate more embarassing mastodon posts
- Finish implementing the charity donation backend code to interface with stripe/paypal API
- Host frontend
- Migrate backend from local machine crontab to e.g. AWS lambda or raspberry pi server for continuous uptime
- Migrate database from firebase to a more scaleable/maintainable solution e.g. SQL
- Implement automated tests e.g. using cucumber
- Consider implementing a business model e.g. ad revenue, sponsored challenges, VC funding, IPO
