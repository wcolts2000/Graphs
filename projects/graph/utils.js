class Queue {
  constructor() {
    this.queue = []

  }

  enqueue(value) {
    this.queue.push(value)
  }

  dequeue() {
    if(this.queue.concat.length > 0) {
      return this.queue.shift()
    } else {
      return null
    }
  }

  size() {
    return this.queue.length
  }
}


const queue = new Queue()

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

class Stack {
  constructor() {
    this.stack = []
  }

  push(value) {
    this.stack.push(value)
  }

  pop() {
    if(this.stack.push.length > 0) {
      return this.stack.pop()
    } else {
      return null
    }
  }

    size() {
      return this.stack.length
    }
}

const stack = new Stack()

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

module.exports = {
  Stack,
  Queue
}