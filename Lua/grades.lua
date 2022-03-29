--require "getStudents.lua"

function newStudent(new_name, new_age, new_grades)
	if new_name == "" or new_name == nil then
		return nil
	end -- will return nil if no name is supplied.
	return { name = new_name, age = new_age, grades = new_grades }
end

function getNewStudent()
	local new_name = ""
	while new_name == "" do
		io.write("Name: ")
		new_name = io.read("*l")
	end -- names are required!
	io.write("Age: ")
	local new_age = io.read("*l")
	io.write("Math Grade: ")
	local new_Math = io.read("*l")
	io.write("Science Grade: ")
	local new_Science = io.read("*l")
	io.write("ELA Grade: ")
	local new_ELA = io.read("*l")
	return newStudent(new_name, new_age, { Math = new_Math, Science = new_Science, ELA = new_ELA })
end

function printGrades(student)
	print(student.name .. "'s' Grades are:\n")
	for subject, grade in pairs(student.grades) do
		if grade == "" then
			print("No Grade Set for " .. subject)
		else
			print(subject .. ": " .. grade .. "%")
		end
	end
end

--local students = getAllStudents()
Student = getNewStudent()
printGrades(Student)
