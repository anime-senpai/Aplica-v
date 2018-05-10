#!/bin/bash
while true; do
	echo
	echo "-------------------------------------------------------------------------"
	echo
	echo "ALGORITMOS"
	echo "1. Depth First Search - dfs"
	echo "2. Breadth First Search - bfs"
	echo "3. Iterative deeping search - ids"
	echo "4. Bidirectional search - bs"
	echo "5. A* Search - astar"
	echo "6. Greedy Search - gs"
	echo "TODOS CONSECUTIVAMENTE EN UN MAPA"
	echo "7. En mediumCorners"
	echo "8. En bigCorners"
	echo "0. SALIR"
	echo
	printf "Selecciones opcion para la ejecución (número + [ENTER]): "
	read option

	if [ "$option" = "0" ]; then
		echo
		exit 0
	elif [ "$option" = "7" ]; then
		echo
		python2 pacman.py -l mediumCorners -p SearchAgent -a fn=dfs,prob=CornersProblem
		echo
		python2 pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
		echo
		python2 pacman.py -l mediumCorners -p SearchAgent -a fn=it,prob=CornersProblem
		echo
		python2 pacman.py -l mediumCorners -p SearchAgent -a fn=BidirectionalSearch,prob=CornersProblem
		echo
		python2 pacman.py -l mediumCorners -p AStarCornersAgent
		echo
		python2 pacman.py -l mediumCorners -p CornersGreedySearchAgent
		echo
		continue
	elif [ "$option" = "8" ]; then
		echo
		python2 pacman.py -l bigCorners -p SearchAgent -a fn=dfs,prob=CornersProblem -z 0.6
		echo
		python2 pacman.py -l bigCorners -p SearchAgent -a fn=bfs,prob=CornersProblem -z 0.6
		echo
		python2 pacman.py -l bigCorners -p SearchAgent -a fn=it,prob=CornersProblem -z 0.6
		echo
		python2 pacman.py -l bigCorners -p SearchAgent -a fn=BidirectionalSearch,prob=CornersProblem -z 0.6
		echo
		python2 pacman.py -l bigCorners -p AStarCornersAgent -z 0.6
		echo
		python2 pacman.py -l bigCorners -p CornersGreedySearchAgent -z 0.6
		echo
		continue
	fi

	echo
	echo "MAPAS"
	echo "a. tinyCorners"
	echo "b. mediumCorners"
	echo "c. bigCorners"
	echo
	printf "Seleccione el mapa donde ejecutar el algoritmo (letra + [ENTER]): "
	read map

	echo

	if [ "$option" = "1" ]; then
		if [ "$map" = "a" ]; then
			python2 pacman.py -l tinyCorners -p SearchAgent -a fn=dfs,prob=CornersProblem
		elif [ "$map" = "b" ]; then
			python2 pacman.py -l mediumCorners -p SearchAgent -a fn=dfs,prob=CornersProblem
		elif [ "$map" = "c" ]; then
			python2 pacman.py -l bigCorners -p SearchAgent -a fn=dfs,prob=CornersProblem -z 0.75
		fi
	elif [ "$option" = "2" ]; then
		if [ "$map" = "a" ]; then
			python2 pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
		elif [ "$map" = "b" ]; then
			python2 pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
		elif [ "$map" = "c" ]; then
			python2 pacman.py -l bigCorners -p SearchAgent -a fn=bfs,prob=CornersProblem -z 0.75
		fi
	elif [ "$option" = "3" ]; then
		if [ "$map" = "a" ]; then
			python2 pacman.py -l tinyCorners -p SearchAgent -a fn=it,prob=CornersProblem
		elif [ "$map" = "b" ]; then
			python2 pacman.py -l mediumCorners -p SearchAgent -a fn=it,prob=CornersProblem
		elif [ "$map" = "c" ]; then
			python2 pacman.py -l bigCorners -p SearchAgent -a fn=it,prob=CornersProblem -z 0.75
		fi
	elif [ "$option" = "4" ]; then
		if [ "$map" = "a" ]; then
			python2 pacman.py -l tinyCorners -p SearchAgent -a fn=BidirectionalSearch,prob=CornersProblem
		elif [ "$map" = "b" ]; then
			python2 pacman.py -l mediumCorners -p SearchAgent -a fn=BidirectionalSearch,prob=CornersProblem
		elif [ "$map" = "c" ]; then
			python2 pacman.py -l bigCorners -p SearchAgent -a fn=BidirectionalSearch,prob=CornersProblem -z 0.75
		fi
	elif [ "$option" = "5" ]; then
		if [ "$map" = "a" ]; then
			python2 pacman.py -l tinyCorners -p AStarCornersAgent
		elif [ "$map" = "b" ]; then
			python2 pacman.py -l mediumCorners -p AStarCornersAgent
		elif [ "$map" = "c" ]; then
			python2 pacman.py -l bigCorners -p AStarCornersAgent -z 0.75
		fi
	elif [ "$option" = "6" ]; then
		if [ "$map" = "a" ]; then
			python2 pacman.py -l tinyCorners -p CornersGreedySearchAgent
		elif [ "$map" = "b" ]; then
			python2 pacman.py -l mediumCorners -p CornersGreedySearchAgent
		elif [ "$map" = "c" ]; then
			python2 pacman.py -l bigCorners -p CornersGreedySearchAgent -z 0.75
		fi
	else
		echo "Ingrese una opción válida de la lista"
	fi
done
