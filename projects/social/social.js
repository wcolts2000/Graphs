class Queue {
  constructor() {
    this.queue = []
  }

  enqueue (value) {
    this.queue.push(value)
  }
  dequeue() {
    if (this.size() > 0 ) {
      return this.queue.shift()
    } else {
      return null
    }
  }
  size () {
    return this.queue.length
  }
}

class User {
  constructor(name) {
    this.name = name
  }
}

class SocialGraph {
  constructor() {
    this.lastId = 0
    this.users = {}
    this.friendships = {}
  }

  addFriendship(userId, friendId) {
    if (userId === friendId) {
      console.log("WARNING: You cannot be friends with yourself")
    } else if (this.friendships[userId].has(userId) || this.friendships[friendId].has(userId) ) {
      console.log("WARNING: Friendship already exists")
    } else {
      this.friendships[userId].add(friendId)
      this.friendships[friendId].add(userId)
    }
  }

  addUser(name) {
    this.lastId++
    this.users[this.lastId] = new User(name)
    this.friendships[this.lastId] = new Set()
  }

  populateGraph(numUsers, avgFriendships) {
    this.lastId = 0
    this.users = {}
    this.friendships = {}

    for (let i = 0; i < numUsers; i++) {
      this.addUser(`User ${i+1}`)
    }

    const possibleFriendships = []

    for (let key in this.users) {
      for (let i = Number(key) + 1; i < this.lastId + 1; i++) {
        possibleFriendships.push([Number(key), i])
        console.log(key)
      }
    }

    console.log("Possible Friendships:")
    console.log(possibleFriendships)
    this.fisherYatesShuffle(possibleFriendships)
    console.log("randmized Friendships:")
    console.log(possibleFriendships)
    
    let totalFriendships = Math.floor(avgFriendships * numUsers / 2)
    console.log("Friendships to create: " + totalFriendships)
    for (let i = 0; i < totalFriendships; i++) {
      let friendship = possibleFriendships[i]
      this.addFriendship(friendship[0], friendship[1])
    }

  }

  fisherYatesShuffle (arr) {
    let i = arr.length;
    if (i === 0) return false;
    while ( --i ) {
      let j = Math.floor( Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]]
    }
    return arr
  }

  getAllSocialPaths (userId) {
    let visited = {},
        longestChain = 0,
        queue = new Queue();
    
        queue.enqueue([userId])

        while (queue.size() > 0) {
          let friendshipConnections = queue.dequeue(),
              currentNode = friendshipConnections[friendshipConnections.length - 1];
              
              if (visited[currentNode] === undefined) {
                visited[currentNode] = friendshipConnections
              }
              
              console.log(this.friendships[currentNode])
              for (const friend of this.friendships[currentNode]) {
            if (!friendshipConnections.includes(friend)) {
              let newFriendConnections = [...friendshipConnections]
              newFriendConnections.push(friend)
              queue.enqueue(newFriendConnections)

              if (queue.size() > longestChain) {
                longestChain = queue.size()
              }
            }
          }          
        }
        console.log(`Friendship connections for ${this.users[userId]}:`)
        console.log(visited)
        return visited
      }
}

let arr = [1,2,3,4,5,6,7,8]


user = new User('sean')
socialG = new SocialGraph()
socialG.populateGraph(10, 2)
console.log('Users:')
console.log(socialG.users)
console.log('Friendships:')
console.log(socialG.friendships)
console.log(socialG.fisherYatesShuffle(arr))
let connections = socialG.getAllSocialPaths(1)
console.log(connections)