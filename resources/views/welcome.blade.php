<!doctype html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    @vite('resources/css/app.css')
</head>

<body>
    <div class="border-2 flex flex-row justify-between items-stretch">
        <img class="border-2 border-red-50 w-3/12" src="{{asset("images/EcoSteps_logo.png")}}" alt="" srcset="">
        <h1 class="border-2 border-red-50 text-3xl font-bold underline text-center self-center"> EcoSteps</h1>
        <img class="border-2 border-red" src="" alt="user-profile" srcset="">
    </div>

    <div class="mx-10 mt-3 pb-4 bottom-2 border-b-2 border-red-400">
        <canvas id="myChart"></canvas>
    </div>

    <div class="mt-3 mx-10  flex justify-between border-b-2 pb-4 border-red-400">
        <div class="border-2 border-red-400 rounded-xl w-2/6 p-2">
            <canvas id="pieChart"></canvas>
        </div>
        <div class="border-2 border-red-400 rounded-xl w-3/6 p-3">
            <h6 class="font-semibold pb-2">Total Steps:</h6>
            <ul>
                <li>Today So Far:</li>
                <li>Past Month:</li>
                <li>This Year:</li>
            </ul>
        </div>
    </div>
    <div class="mx-10 mt-3 pb-4 bottom-2 border-b-2 border-red-400 flex flex-row justify-between items-stretch">
        div
    </div>
</body>

@vite('resources/js/app.js')

</html>