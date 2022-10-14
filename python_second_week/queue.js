class Queue {
  constructor(list,limit){
    this.list = []
    this.limit = 10
  }
  
  add(e) {
    if (this.list.length < this.limit) {
      this.list.push(e)
      return true
    }
    return false
  }
  
  element() {
    return this.list[0]
  }
  
  offer1(e) {
    this.list.push(e)
    return true
  }
  
  offer2(e) {
    if (this.list.length >= this.limit) {
      this.list.pop()
      this.list.push(e)
      return true
    }
    return false
  }
  
  peek() {
    if (this.list.length === 0) {
      return null
    }
    return this.list[0]
  }
  
  pool() {
    if (this.list.length === 0) {
      return null
    }
    const aux = this.list[0]
    this.list.shift()
    return aux
  }
  
  remove() {
    const aux = this.list[0]
    this.list.shift()
    return aux
  }
  
  size() {
    return this.list.length
  }
  
  is_empty() {
    return this.list.length === 0
  }
}

const proob = new Queue;

console.log(proob.peek())

console.log(proob.pool())

console.log(proob.remove())

console.log(proob.size())

console.log(proob.is_empty())

proob.add(1)
proob.add(2)
proob.add(3)
proob.add(4)
proob.add(5)
proob.add(6)
proob.add(7)
proob.add(8)
proob.add(9)
proob.add(10)
proob.add(11)

console.log(proob.element())

console.log(proob.offer1(12))
console.log(proob.offer2(13))

console.log(proob.peek())

console.log(proob.pool())

console.log(proob.remove())

console.log(proob.size())

console.log(proob.is_empty())

console.log(proob.list)