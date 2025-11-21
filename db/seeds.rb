# Clear existing data
puts "Cleaning database..."
Appointment.destroy_all
DoctorProfile.destroy_all
User.destroy_all
Department.destroy_all

puts "Creating Departments..."
cardiology = Department.create!(name: 'Kardiyoloji')
internal_med = Department.create!(name: 'Dahiliye')
orthopedics = Department.create!(name: 'Ortopedi')

puts "Creating Doctors..."
dr_ahmet = User.create!(
  name: 'Dr. Ahmet Yılmaz',
  email: 'ahmet@example.com',
  password: '123123',
  password_confirmation: '123123',
  role: :doctor
)
DoctorProfile.create!(
  user: dr_ahmet,
  department: cardiology,
  room_number: '101',
  bio: 'Uzman Kardiyolog, 10 yıllık tecrübe.'
)

dr_selin = User.create!(
  name: 'Dr. Selin Kaya',
  email: 'selin@example.com',
  password: '123123',
  password_confirmation: '123123',
  role: :doctor
)
DoctorProfile.create!(
  user: dr_selin,
  department: internal_med,
  room_number: '102'
)

dr_mehmet = User.create!(
  name: 'Dr. Mehmet Tunç',
  email: 'mehmet@example.com',
  password: '123123',
  password_confirmation: '123123',
  role: :doctor
)
DoctorProfile.create!(
  user: dr_mehmet,
  department: orthopedics,
  room_number: '103'
)

puts "Creating Patients..."
ayse = User.create!(
  name: 'Ayşe Demir',
  email: 'ayse@example.com',
  password: '123123',
  password_confirmation: '123123',
  role: :patient
)

ali = User.create!(
  name: 'Ali Korkmaz',
  email: 'ali@example.com',
  password: '123123',
  password_confirmation: '123123',
  role: :patient
)

puts "Creating Admin..."
User.create!(
  name: 'Admin Kullanıcı',
  email: 'admin@example.com',
  password: 'admin123',
  password_confirmation: 'admin123',
  role: :admin
)

puts "Creating Appointments..."
Appointment.create!(
  patient: ayse,
  doctor: dr_ahmet,
  scheduled_at: Time.current.change(hour: 10, min: 0),
  status: :pending,
  note: 'Kalp çarpıntısı şikayeti.'
)

Appointment.create!(
  patient: ali,
  doctor: dr_selin,
  scheduled_at: Time.current.change(hour: 14, min: 0),
  status: :pending,
  note: 'Rutin kontrol.'
)

puts "Seeding completed successfully!"
