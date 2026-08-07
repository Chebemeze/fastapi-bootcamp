function Welcome() {
    return (
        <h1>Hello World</h1>
    );
}
 const message = Welcome()
console.log(message)

welcome = ()=> "Hello World"

function EmployeeCard() {
    return (
        <div>
            <h2>Eze Chukwuchebem Ebenezer</h2>
            <p>Mechanical Engineer</p>
            <p>Perfomance rating: 98%</p>
        </div>
    );
}


function EmployeeProfile() {
    const employee = {
        name: "Grace",
        role: "Product Manager",
        department: "Technology",
        score: 92
    };

    return (
        <>
            <p>Name: {employee.name}</p>
            <p>Role: {employee.role}</p>
            <p>Department: {employee.department}</p>
            <p>Performance score: {employee.score}</p>
        </>
    );
}