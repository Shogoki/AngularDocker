export class Server {
    constructor(
     public  applier: string,
     public id: number,
     public owner: string,
     public purpose: string,
     public responsible: string,
     public servername: string
    ) {}
 }