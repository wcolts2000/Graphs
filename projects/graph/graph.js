const helpers = require('./utils')

class Graph {
  constructor() {
    this.vertices = {}
  }

  addVertex(vertex) {
    this.vertices[vertex] = new Set()
  }

  addEdge(v1, v2) {
    // console.log(`this vertices: ${JSON.stringify(this.vertices)}`)
    // console.log(`v1: ${v1}, v2: ${v2}`)
    if (Object.keys(this.vertices).includes(`${v1}`) && Object.keys(this.vertices).includes(`${v2}`)) {
      this.vertices[v1].add(v2)
    } else {
      throw new Error("That vertex does not exist")
    }
  }

  bft(startingVertex) {
    const queue = new helpers.Queue()
    queue.enqueue(startingVertex)

    const visited = new Set()

    while (queue.size() > 0) {
      const v = queue.dequeue()

      if (!visited.has(v)) {
        console.log(v)
        visited.add(v)

        for (const neighbor of this.vertices[v]) {
          queue.enqueue(neighbor)
        }
      }
    }
  }

  dft(startingVertex) {
    const stack = new helpers.Stack()
    stack.push(startingVertex)

    const visited = new Set()

    while (stack.size() > 0) {
      const v = stack.pop()

      if(!visited.has(v)) {
        console.log(v)
        visited.add(v)

        for (const neighbor of this.vertices[v]) {
          stack.push(neighbor)
        }
      }
    }
  }

  dftRecursive(startingVertex, visited=null) {
    if(!visited) {
      visited = new Set()
    }

    visited.add(startingVertex)
    console.log("recurse", startingVertex)

    for (const neighbor of this.vertices[startingVertex]) {
      if(!visited.has(neighbor)) {
        this.dftRecursive(neighbor, visited)
      }
    }
  }

  bfs(startingVertex, destinationVertex) {
    // Create an empty queue and enqueue A PATH TO the starting vertex ID
  const queue = new helpers.Queue()

  if (typeof destinationVertex !== 'object') {
    startingVertex = [startingVertex]
  }
  queue.enqueue(startingVertex)
  // Create a Set to store visited vertices
  const visited = new Set()
  // While the queue is not empty...
  while (queue.size() > 0) {
    // Dequeue the first PATH
    const v = queue.dequeue()
    // Grab the last vertex from the PATH
    const lastVertex = v[v.length - 1]
    // If that vertex has not been visited...
    if (!visited.has(lastVertex)) {
      // CHECK IF IT'S THE TARGET
      if(lastVertex === destinationVertex) {
        console.log(`found vertex via ${JSON.stringify(v)}`)
        // IF SO, RETURN PATH
        return v
      }
      // Mark it as visited...
      visited.add(lastVertex)
      // Then add A PATH TO its neighbors to the back of the queue
      for (const neighbor of this.vertices[lastVertex]) {
        // COPY THE PATH
        const newPath = [...v]
        newPath.push(neighbor)
        // APPEND THE NEIGHBOR TO THE BACK
        queue.enqueue(newPath)
      }
    }
  }
  return false
  }


  dfs(startingVertex, destinationVertex) {
    // Create an empty queue and enqueue A PATH TO the starting vertex ID
  const stack = new helpers.Stack()

  if (typeof destinationVertex !== 'object') {
    startingVertex = [startingVertex]
  }
  stack.push(startingVertex)
  // Create a Set to store visited vertices
  const visited = new Set()
  // While the stack is not empty...
  while (stack.size() > 0) {
    // pop the first PATH
    const v = stack.pop()
    // Grab the last vertex from the PATH
    const lastVertex = v[v.length - 1]
    // If that vertex has not been visited...
    if (!visited.has(lastVertex)) {
      // CHECK IF IT'S THE TARGET
      if(lastVertex === destinationVertex) {
        console.log(`found vertex via ${JSON.stringify(v)}`)
        // IF SO, RETURN PATH
        return v
      }
      // Mark it as visited...
      visited.add(lastVertex)
      // Then add A PATH TO its neighbors to the back of the stack
      for (const neighbor of this.vertices[lastVertex]) {
        // COPY THE PATH
        const newPath = [...v]
        newPath.push(neighbor)
        // APPEND THE NEIGHBOR TO THE BACK
        stack.push(newPath)
      }
    }
  }
  return false
  }

}

const graph = new Graph()

graph.addVertex(1)
graph.addVertex(2)
graph.addVertex(3)
graph.addVertex(4)
graph.addVertex(5)
graph.addVertex(6)
graph.addVertex(7)
graph.addEdge(5,3)
graph.addEdge(6,3)
graph.addEdge(7,1)
graph.addEdge(4,7)
graph.addEdge(1,2)
graph.addEdge(7,6)
graph.addEdge(2,4)
graph.addEdge(3,5)
graph.addEdge(2,3)
graph.addEdge(4,6)

console.log(graph.vertices)
console.log( "\n=================\n")

graph.bft(1)
console.log( "\n=================\n")

graph.dft(1)
console.log( "\n=================\n")

graph.dftRecursive(1)
console.log( "\n=================\n")

console.log(graph.bfs(1,6))
console.log( "\n=================\n")

console.log(graph.dfs(1,6))
console.log( "\n=================\n")






// const stack = new helpers.Stack()
// stack.push(1)
// stack.push(2)
// stack.push(3)
// stack.push(4)
// console.log(stack, stack.size())
// stack.pop()
// console.log(stack, stack.size())
// stack.pop()
// console.log(stack, stack.size())
// stack.pop()
// console.log(stack, stack.size())
// stack.pop()
// console.log(stack, stack.size())

// const queue = new helpers.Queue()
// queue.enqueue(1)
// queue.enqueue(2)
// queue.enqueue(3)
// queue.enqueue(4)
// console.log(queue, queue.size())
// queue.dequeue()
// console.log(queue, queue.size())
// queue.dequeue()
// console.log(queue, queue.size())
// queue.dequeue()
// console.log(queue, queue.size())
// queue.dequeue()
// console.log(queue, queue.size())