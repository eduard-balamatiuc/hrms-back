-- Populate patient_user table
INSERT INTO public.patient_user (id, "IDNP", mail, password, name, surname, location, phone, image_uri)
VALUES
('d290f1ee-6c54-4b01-90e6-d701748f0851', '1234567890123', 'john.doe@example.com', 'password123', 'John', 'Doe', '123 Main St, Anytown', 1234567890, 'http://example.com/john_doe.jpg'),
('f290f1ee-6c54-4b01-90e6-d701748f0852', '9876543210123', 'jane.smith@example.com', 'password456', 'Jane', 'Smith', '456 Elm St, Othertown', 1987654321, 'http://example.com/jane_smith.jpg');

-- Populate doctor_user table
INSERT INTO public.doctor_user (id, "IDNP", name, surname, mail, password, location, phone, image_uri)
VALUES
('e290f1ee-6c54-4b01-90e6-d701748f0853', '2468101214161', 'Dr. Alice', 'Johnson', 'alice.johnson@hospital.com', 'password789', '789 Health St, MedCity', 1231231234, 'http://example.com/alice_johnson.jpg'),
('c290f1ee-6c54-4b01-90e6-d701748f0854', '1357911131517', 'Dr. Bob', 'Williams', 'bob.williams@hospital.com', 'password101', '456 Health St, MedCity', 9876543210, 'http://example.com/bob_williams.jpg');

-- Populate general_information table
INSERT INTO public.general_information (id, patient_user_id, height, weight, blood_type, gender, date_of_birth)
VALUES
('b290f1ee-6c54-4b01-90e6-d701748f0855', 'd290f1ee-6c54-4b01-90e6-d701748f0851', 180, 75, 'O+', 'Male', '1985-01-15'),
('a290f1ee-6c54-4b01-90e6-d701748f0856', 'f290f1ee-6c54-4b01-90e6-d701748f0852', 165, 60, 'A+', 'Female', '1990-02-20');

-- Populate appointments table
INSERT INTO public.appointments (id, patient_user_id, doctor_user_id, start_datetime, end_datetime, comments)
VALUES
('3cd2c678-d176-4d7b-82a9-5aa77e5c1c70', 'd290f1ee-6c54-4b01-90e6-d701748f0851', 'e290f1ee-6c54-4b01-90e6-d701748f0853', '2024-09-01', '2024-09-01', 'Annual checkup'),
('2c908c49-194f-4954-9889-85ae7207b8cf', 'f290f1ee-6c54-4b01-90e6-d701748f0852', 'c290f1ee-6c54-4b01-90e6-d701748f0854', '2024-09-05', '2024-09-05', 'Consultation for knee pain');