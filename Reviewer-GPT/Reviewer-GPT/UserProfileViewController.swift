//
//  UserProfileViewController.swift
//  Reviewer-GPT
//
//  Created by kakao on 1/17/25.
//

import UIKit

class UserProfileViewController: UIViewController {
    
    private let viewModel: UserViewModel
    
    init(viewModel: UserViewModel) {
        self.viewModel = viewModel
        super.init(nibName: nil, bundle: nil)
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    private let nameLabel = UILabel()
    private let emailLabel = UILabel()
    private let bioLabel = UILabel()
    private let updateButton = UIButton(type: .system)
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        view.backgroundColor = .white
        setupViews()
        updateUI()
    }
    
    private func setupViews() {
        nameLabel.translatesAutoresizingMaskIntoConstraints = false
        emailLabel.translatesAutoresizingMaskIntoConstraints = false
        bioLabel.translatesAutoresizingMaskIntoConstraints = false
        updateButton.translatesAutoresizingMaskIntoConstraints = false
        
        view.addSubview(nameLabel)
        view.addSubview(emailLabel)
        view.addSubview(bioLabel)
        view.addSubview(updateButton)
        
        updateButton.setTitle("Update Bio", for: .normal)
        updateButton.addTarget(self, action: #selector(updateBio), for: .touchUpInside)
        
        NSLayoutConstraint.activate([
            nameLabel.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 20),
            nameLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            
            emailLabel.topAnchor.constraint(equalTo: nameLabel.bottomAnchor, constant: 10),
            emailLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            
            bioLabel.topAnchor.constraint(equalTo: emailLabel.bottomAnchor, constant: 10),
            bioLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            
            updateButton.topAnchor.constraint(equalTo: bioLabel.bottomAnchor, constant: 20),
            updateButton.centerXAnchor.constraint(equalTo: view.centerXAnchor)
        ])
    }
    
    private func updateUI() {
        nameLabel.text = "Name: \(viewModel.user.name)"
        emailLabel.text = "Email: \(viewModel.user.email)"
        bioLabel.text = "Bio: \(viewModel.user.bio)"
    }
    
    @objc private func updateBio() {
        let alert = UIAlertController(title: "Update Bio", message: "Enter new bio", preferredStyle: .alert)
        alert.addTextField { textField in
            textField.placeholder = "New bio"
        }
        let updateAction = UIAlertAction(title: "Update", style: .default) { [weak self] _ in
            guard let newBio = alert.textFields?.first?.text, !newBio.isEmpty else { return }
            self?.viewModel.updateBio(newBio)
            self?.updateUI()
        }
        alert.addAction(updateAction)
        alert.addAction(UIAlertAction(title: "Cancel", style: .cancel))
        present(alert, animated: true)
    }
}
