<!doctype html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">

    @vite('resources/css/app.css')
</head>

<body>
    <div class="border-b-2 top-0 backdrop-blur-2xl border-yellow-500 fixed flex flex-row justify-between items-stretch">

        <img class=" w-3/12 h-3/12" src="{{asset("images/EcoSteps_logo.png")}}" alt="" srcset="">
        <h1 class=" text-2xl font-bold underline text-center self-center"> EcoSteps</h1>
        <div class="rounded-full w-[150px] h-[150px] overflow-hidden">
            <img class=" object-cover relative bottom-5" src="{{asset("images/headhost.jpeg")}}" alt="user-profile" srcset="">
        </div>
    </div>

    <div class="mx-10 mt-48 pb-4 bottom-2 border-b-4 border-sky-950">
        <canvas id="myChart"></canvas>
    </div>

    <div class="mt-3 mx-10 flex justify-between pb-4 ">
        <div class="border-4 border-yellow-500 rounded-xl w-2/6 p-2">
            <canvas id="pieChart"></canvas>
        </div>
        <div class="border-4 border-yellow-500 rounded-xl w-3/6 p-3">
            <h6 class="font-semibold pb-2">Total Steps:</h6>
            <ul>
                <li>Today So Far: <span class="font-bold font-code">1240</span></li>
                <li>Past Month: <span class="font-bold font-code">20345</span></li>
                <li>This Year: <span class="font-bold font-code">10023456098</span></li>
            </ul>
        </div>
    </div>
    <div class="mx-10 mt-3 pb-4 bottom-2 border-4 border-yellow-500 flex flex-row justify-between items-stretch rounded-xl">
        <div class="flex flex-row justify-between p-6">
            <img class="w-3/12" src="{{asset('images/wwf.svg')}}" alt="" srcset="">
            <div class="pl-8">

                <h3 class="mb-4">About WWF</h3>
                <p>We’re WWF, the leading global environmental charity, and we’re bringing our world back to life. With nature in freefall, we’re urgently tackling the underlying causes that are driving the decline, and we’re finding solutions so future generations have a world with thriving habitats and wildlife. It’s a huge challenge, but if we all act together, there is hope.</p>
            </div>
        </div>
    </div>
</body>

@vite('resources/js/app.js')

</html>