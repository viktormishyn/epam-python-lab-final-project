declare -a arr=('Strategy' 'RPG' 'Action'
    'Adventure' 'Simulation' 'Sports' 'Racing')

for i in "${arr[@]}"; do
    curl -u "admin@gmail.com:admin" -X POST http://localhost:8000/api/v1/genres/ -F "name=$i"
done

curl -u "admin@gmail.com:admin" -X POST http://localhost:8000/api/v1/games/ \
    -F "name=Warcraft III: The Frozen Throne" -F 'description=Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean auctor erat id dapibus tristique. Integer fringilla tellus imperdiet, porta diam sit amet, egestas nisl. Proin euismod sit amet urna quis blandit. Donec ut nulla pulvinar, commodo ante eu, tincidunt massa. Aenean eu nisl blandit urna lacinia volutpat id eget dolor. Quisque id tortor ex. Sed lacinia dictum nisl eget porta. Aenean ultrices maximus risus, in pulvinar magna bibendum non. Cras ac tellus dapibus, efficitur diam nec, consequat justo.' \
    -F 'price=20.00' -F 'genre=Strategy' -F "image=@./backend/test_data/warcraft.jpg"

curl -u "admin@gmail.com:admin" -X POST http://localhost:8000/api/v1/games/ \
    -F "name=Counter-Strike: Source" -F 'description=Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean auctor erat id dapibus tristique. Integer fringilla tellus imperdiet, porta diam sit amet, egestas nisl. Proin euismod sit amet urna quis blandit. Donec ut nulla pulvinar, commodo ante eu, tincidunt massa. Aenean eu nisl blandit urna lacinia volutpat id eget dolor. Quisque id tortor ex. Sed lacinia dictum nisl eget porta. Aenean ultrices maximus risus, in pulvinar magna bibendum non. Cras ac tellus dapibus, efficitur diam nec, consequat justo.' \
    -F 'price=20.00' -F 'genre=Action' -F "image=@./backend/test_data/cs.jpg"

curl -u "admin@gmail.com:admin" -X POST http://localhost:8000/api/v1/games/ \
    -F "name=Gothic II: Gold Edition" -F 'description=Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean auctor erat id dapibus tristique. Integer fringilla tellus imperdiet, porta diam sit amet, egestas nisl. Proin euismod sit amet urna quis blandit. Donec ut nulla pulvinar, commodo ante eu, tincidunt massa. Aenean eu nisl blandit urna lacinia volutpat id eget dolor. Quisque id tortor ex. Sed lacinia dictum nisl eget porta. Aenean ultrices maximus risus, in pulvinar magna bibendum non. Cras ac tellus dapibus, efficitur diam nec, consequat justo.' \
    -F 'price=59.99' -F 'genre=RPG' -F "image=@./backend/test_data/gothic.jpg"

curl -u "admin@gmail.com:admin" -X POST http://localhost:8000/api/v1/games/ \
    -F "name=Sid Meier's Civilization V" -F 'description=Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean auctor erat id dapibus tristique. Integer fringilla tellus imperdiet, porta diam sit amet, egestas nisl. Proin euismod sit amet urna quis blandit. Donec ut nulla pulvinar, commodo ante eu, tincidunt massa. Aenean eu nisl blandit urna lacinia volutpat id eget dolor. Quisque id tortor ex. Sed lacinia dictum nisl eget porta. Aenean ultrices maximus risus, in pulvinar magna bibendum non. Cras ac tellus dapibus, efficitur diam nec, consequat justo.' \
    -F 'price=79.99' -F 'genre=Strategy' -F "image=@./backend/test_data/civilization.jpg"

curl -u "admin@gmail.com:admin" -X POST http://localhost:8000/api/v1/games/ \
    -F "name=The Elder Scrolls III: Morrowind" -F 'description=Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean auctor erat id dapibus tristique. Integer fringilla tellus imperdiet, porta diam sit amet, egestas nisl. Proin euismod sit amet urna quis blandit. Donec ut nulla pulvinar, commodo ante eu, tincidunt massa. Aenean eu nisl blandit urna lacinia volutpat id eget dolor. Quisque id tortor ex. Sed lacinia dictum nisl eget porta. Aenean ultrices maximus risus, in pulvinar magna bibendum non. Cras ac tellus dapibus, efficitur diam nec, consequat justo.' \
    -F 'price=29.99' -F 'genre=RPG' -F "image=@./backend/test_data/morrowind.jpg"

curl -u "admin@gmail.com:admin" -X POST http://localhost:8000/api/v1/games/ \
    -F "name=Unreal Tournament 3" -F 'description=Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean auctor erat id dapibus tristique. Integer fringilla tellus imperdiet, porta diam sit amet, egestas nisl. Proin euismod sit amet urna quis blandit. Donec ut nulla pulvinar, commodo ante eu, tincidunt massa. Aenean eu nisl blandit urna lacinia volutpat id eget dolor. Quisque id tortor ex. Sed lacinia dictum nisl eget porta. Aenean ultrices maximus risus, in pulvinar magna bibendum non. Cras ac tellus dapibus, efficitur diam nec, consequat justo.' \
    -F 'price=35.99' -F 'genre=Action' -F "image=@./backend/test_data/unreal_tournament.jpg"

curl -u "admin@gmail.com:admin" -X POST http://localhost:8000/api/v1/games/ \
    -F "name=The Witcher" -F 'description=Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean auctor erat id dapibus tristique. Integer fringilla tellus imperdiet, porta diam sit amet, egestas nisl. Proin euismod sit amet urna quis blandit. Donec ut nulla pulvinar, commodo ante eu, tincidunt massa. Aenean eu nisl blandit urna lacinia volutpat id eget dolor. Quisque id tortor ex. Sed lacinia dictum nisl eget porta. Aenean ultrices maximus risus, in pulvinar magna bibendum non. Cras ac tellus dapibus, efficitur diam nec, consequat justo.' \
    -F 'price=29.99' -F 'genre=RPG' -F "image=@./backend/test_data/witcher.jpg"
