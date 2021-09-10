---
layout: page
title: "Tracking My Range for a Tesla Model Y Charging Solution"
subtitle: How much do I drive?
postdate: 20-Aug-2021
---

I’ve been on the fence about ordering a Level 2 charger, essentially a 240V charger. It gives you a quick recharge, but they are expensive. Tesla offers one for $500, and the other ones I’ve considered are more expensive. I’ve watched a few videos on whether it makes sense, trying to decide, but one of the interesting things I’ve seen people talk about is how far you drive and how often.

This is really to decide what type of charging I need to mess with. Do I live with 110, normal US outlet. Use a 220V outlet or get a charging device.

Tl;dr – I found that often a 110 would charge me across a couple days, but in a busy week I might be losing mileage. That leads me to think a 220V charging system is needed. I also am bad about carrying things with me, so I don’t want to depend on remembering to bring my cable and adapters. As a result, I bought the Tesla charger.

## Building a System to Capture Data

Tracking data is something we want to do automatically where possible, but since I have an older 2012 car, I can’t easily access the mileage at any time. I also don’t have a great way to track when the car has some home and when it leaves.

I don’t care about individual trips, as I’m unlikely to charge on the road when I’m near the house. If I go to the mountains, perhaps I’ll charge, but not on many other trips.

The data I wanted to capture was this:

- start mileage
- end mileage
- time to next trip

I started an Evernote note to track this and tried to fill it out, but I wasn’t great at following the process. I forgot to open Evernote and write things down too often. Plus, entering numbers and times and dates proved to be cumbersome on a mobile.

The best was to do this was to create an Excel sheet and walk back to the car to grab mileage. Or text myself the current mileage (or start/end time) for a trip. Then I could easily enter the three values above in my Excel sheet.

I ended up with a sheet that looks like this:

![Spreadsheet of driving data](/assets/img/cars/drivingdata.png)

From left to right, these are the columns:

- Date
- Mileage start
- Mileage end
- start time (usually skipped)
- end time (usually skipped)
- Total mileage (subtract the items above)
- Time to next trip (hours until I left again)
- Charging surplus or deficit in time at different levels (4 columns)

This worked well, but I struggled to actually get the mileage into the sheet on my phone. As a result, I decided to do this a fairly simple way. I put a reminder in my car.

![reminding me to track mileage](reminder.png)

The helped me remember to track the end mileage and go type it in when I returned home.

## Computing Charge Time

The various charging methods result in different recovery for range across time. This was a little confusing to think about at first, but essentially, based on charts from Tesla and others, I went with this idea. If I charge in these ways, here is the range I recovery in an hour:

- US 110V outlet – 4mph
- US 220V/30A plug – 22mph
- US 220V/50A – 30mph
- Tesla Wall Charger – 42mph

We don’t think about time with petrol cars. The difference between adding 5 gallons and 20 gallons is a tiny amount of time at a filling station, so it’s really cost there. However, for electric, time matters, because adding a “full tank” could be hours.

My computation in the sheet is based in the mileage driven. I take that as the amount of charge I want to recover. To determine if I do that, I take the mileage and divide by the various charge amounts above.

In Excel, this looks like =+G18-(F18/$H$2) for the 18th row. As a better example, supposed I went 40 miles on a trip, and I had 1 hour to charge before my next trip. I’d end up with these values for my charging columns:

- US 110V outlet – 9 hours (red)
- US 220V/30A plug – .82 hours (red)
- US 220V/50A – .33 hours (red)
- Tesla Wall Charger – 0.05 hours (green)

The red numbers mean I wouldn’t have recovered my mileage before the next trip. The green numbers mean I wouldn’t. The value tells me how much time I’d need to recover the charge. For the example above, I’d need 9 more hours, 10 total, to recover from a 40 mile trip. For the Tesla Wall Charger (TWC), I’d have recovered with 0.05 hours to spare.

## Analysis

On most days, before trips the next day, I’d have recovered charge using 110. Not always, but most days. Not all trips, but across days. Often across two days, I’d certainly recover. However, this is in the summer, not winter, and I definitely have a different pattern in the winter, with volleyball practices and tournaments, not to mention more heating while sitting in the car.

The concerning trips were a few 70-100mi days, which do happen regularly for me in the winter, where I wouldn’t have recovered in 20 hours.

I do have a 220v/30A plug in the garage for a house vacuum that I never use. I also was considering the NEMA 14-50 plug, which is 200V/50A. However, with both those, I’d need to use the cable that came with the car, which means it wouldn’t be back in the car unless I put it there.

A friend noted that I wouldn’t often use the cable unless I was at someone else’s house or at a campground. A campground is possible for me as a place I might go, and possibly friend’s houses, but likely I’d be looking for a Supercharger or a public station. I also think I might see if I could get the condo association to make a plug available in Keystone for me, which means I’d definitely want the mobile cable.

Knowing how Murphy’s Law strikes with me often, I’m not thrilled with the idea of not having a cable with me. I could buy a second one, but that’s a US$520 charge, as opposed to the US$500 Wall charger. An adapter set is also $220, which seems pricey. I could get the single NEMA adapter for US$35-45, but with my concern about Murphy’s Law, I don’t know that makes sense.

My wife said we shouldn’t take chances here, and knowing that we might have a couple trips in a few days. Me going to speak in CO Springs and then a volleyball tournament the next day, or going skiing and then having another trip the next day. We’d want to recover 200 miles in an 8-10 hour window.

There’s another thought. The US Tax code gives a [30% tax credit](https://www.irs.gov/pub/irs-pdf/f8911.pdf) on the cost of electric charging.

As a result, I decided to just by the Tesla Wall Charger. This ended up being US$514.50, and I’ve contacted an electrician to add a new breaker and wire this up. It will be a short wiring run for me, but even if this is a $200 cost, I’ll end up with this being a $500 cost, as the tax credit will cover the install.

I did look at other chargers, and I’ll do a post summarizing what I learned and decided on.

Next: [Date Slippage in the Tesla Model Y Order Process](/projects/tesla/dateslip/)

If you are thinking of ordering one, I’ve got a referral code. You get 1,000 free Supercharger miles and so do I. Use: [http://ts.la/john92950](http://ts.la/john92950)